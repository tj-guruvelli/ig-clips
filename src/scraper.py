"""
Clip Scraper
Uses Playwright (browser automation) and optionally Firecrawl API.
Searches Instagram and X for AI podcast/interview clips.
"""

import asyncio
import logging
import os
import re
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

log = logging.getLogger(__name__)

try:
    from playwright.async_api import async_playwright, Page, Browser
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    log.warning("Playwright not installed — browser scraping disabled")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class ClipScraper:
    def __init__(
        self,
        instagram_user: Optional[str] = None,
        instagram_pass: Optional[str] = None,
        firecrawl_key: Optional[str] = None,
    ):
        self.instagram_user = instagram_user
        self.instagram_pass = instagram_pass
        self.firecrawl_key = firecrawl_key
        self._browser: Optional[Browser] = None
        self._page: Optional[Page] = None

    # ── Lifecycle ────────────────────────────────────────────────────────────

    async def _start_browser(self):
        if not PLAYWRIGHT_AVAILABLE:
            raise RuntimeError("Playwright is not installed")
        self._pw = await async_playwright().start()
        self._browser = await self._pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        context = await self._browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
        )
        self._page = await context.new_page()

    async def _stop_browser(self):
        if self._browser:
            await self._browser.close()
        if hasattr(self, "_pw"):
            await self._pw.stop()

    # ── Instagram ────────────────────────────────────────────────────────────

    async def _instagram_login(self):
        if not self.instagram_user or not self.instagram_pass:
            log.warning("Instagram credentials not set — skipping login")
            return
        page = self._page
        await page.goto("https://www.instagram.com/accounts/login/", timeout=30000)
        await page.wait_for_timeout(2000)
        await page.fill('input[name="username"]', self.instagram_user)
        await page.fill('input[name="password"]', self.instagram_pass)
        await page.click('button[type="submit"]')
        await page.wait_for_timeout(5000)
        log.info("Instagram login attempted")

    async def _instagram_search(self, query: str) -> List[Dict]:
        clips = []
        page = self._page
        search_url = f"https://www.instagram.com/explore/search/keyword/?q={query.replace(' ', '+')}"
        try:
            await page.goto(search_url, timeout=20000)
            await page.wait_for_timeout(3000)

            # Collect reel links visible on the page
            links = await page.eval_on_selector_all(
                "a[href*='/reel/']",
                "els => els.map(e => e.href)"
            )
            for link in links[:10]:  # cap per query to avoid rate limits
                clip = await self._instagram_reel_details(link)
                if clip:
                    clips.append(clip)
                await page.wait_for_timeout(800)
        except Exception as e:
            log.warning("Instagram search error [%s]: %s", query, e)
        return clips

    async def _instagram_reel_details(self, url: str) -> Optional[Dict]:
        page = self._page
        try:
            await page.goto(url, timeout=15000)
            await page.wait_for_timeout(2000)

            views_text = await page.inner_text("span.x193iq5w", timeout=5000).catch(lambda _: "")
            caption = await page.inner_text("div._a9zs", timeout=5000).catch(lambda _: "")
            duration_text = await page.inner_text("span._acb4", timeout=5000).catch(lambda _: "")

            views = _parse_views(views_text)
            duration = _parse_duration(duration_text)
            speaker = _extract_speaker(caption)
            topic = _extract_topic(caption)

            return {
                "url": url,
                "platform": "instagram",
                "views": views,
                "duration_sec": duration,
                "caption": caption,
                "speaker": speaker,
                "topic": topic,
                "format": _detect_format(caption),
                "posted_date": None,  # Instagram hides exact dates; will be estimated
                "original_source": _extract_source(caption),
                "full_episode_link": "",
                "interview_date": None,
                "credits_handle": _extract_credits_handle(caption),
                "already_on_brainsbyai": "No",
                "already_on_competitor": "No",
            }
        except Exception as e:
            log.debug("Could not fetch reel details [%s]: %s", url, e)
            return None

    async def _instagram_audit_account(self, handle: str) -> List[Dict]:
        """Pull recent reels from an account to build the brainsbyai exclusion list."""
        clips = []
        page = self._page
        try:
            await page.goto(f"https://www.instagram.com/{handle}/reels/", timeout=20000)
            await page.wait_for_timeout(3000)
            links = await page.eval_on_selector_all(
                "a[href*='/reel/']",
                "els => els.map(e => e.href)"
            )
            for link in set(links):
                clips.append({"url": link, "platform": "instagram"})
        except Exception as e:
            log.warning("Could not audit @%s: %s", handle, e)
        return clips

    # ── X / Twitter ──────────────────────────────────────────────────────────

    async def _x_search(self, query: str) -> List[Dict]:
        """Search X for video clips matching the query."""
        clips = []
        page = self._page

        # X video search — filter:videos to get clips only
        search_url = (
            f"https://x.com/search?q={query.replace(' ', '+')}+"
            "filter%3Avideos&src=typed_query&f=live"
        )
        try:
            await page.goto(search_url, timeout=20000)
            await page.wait_for_timeout(4000)

            # Scroll to load more results
            for _ in range(3):
                await page.keyboard.press("End")
                await page.wait_for_timeout(1500)

            # Extract tweet links with videos
            links = await page.eval_on_selector_all(
                "article a[href*='/status/']",
                "els => [...new Set(els.map(e => e.href))]"
            )

            for link in links[:8]:
                clip = await self._x_post_details(link)
                if clip:
                    clips.append(clip)
                await page.wait_for_timeout(600)
        except Exception as e:
            log.warning("X search error [%s]: %s", query, e)
        return clips

    async def _x_post_details(self, url: str) -> Optional[Dict]:
        page = self._page
        try:
            await page.goto(url, timeout=15000)
            await page.wait_for_timeout(2000)

            tweet_text = await page.inner_text("div[data-testid='tweetText']", timeout=5000)
            views_raw = await page.inner_text("span[data-testid='app-text-transition-container']", timeout=5000)
            views = _parse_views(views_raw)

            # Only surface if views >= 1M or >10k likes
            if views < 1_000_000:
                return None

            speaker = _extract_speaker(tweet_text)
            topic = _extract_topic(tweet_text)

            return {
                "url": url,
                "platform": "x",
                "views": views,
                "duration_sec": None,
                "caption": tweet_text,
                "speaker": speaker,
                "topic": topic,
                "format": _detect_format(tweet_text),
                "posted_date": _parse_x_date(page),
                "original_source": _extract_source(tweet_text),
                "full_episode_link": "",
                "interview_date": None,
                "credits_handle": "",
                "already_on_brainsbyai": "No",
                "already_on_competitor": "No",
            }
        except Exception as e:
            log.debug("Could not fetch X post [%s]: %s", url, e)
            return None

    def _parse_x_date(self, page) -> Optional[datetime]:
        try:
            time_el = page.locator("time").first
            dt_attr = time_el.get_attribute("datetime")
            if dt_attr:
                return datetime.fromisoformat(dt_attr.replace("Z", "+00:00"))
        except Exception:
            pass
        return None

    # ── Firecrawl fallback ───────────────────────────────────────────────────

    def _firecrawl_search(self, query: str, site: str = "instagram.com") -> List[Dict]:
        """Firecrawl API-based search as fallback when Playwright is blocked."""
        if not self.firecrawl_key or not REQUESTS_AVAILABLE:
            return []
        try:
            resp = requests.post(
                "https://api.firecrawl.dev/v1/search",
                headers={
                    "Authorization": f"Bearer {self.firecrawl_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "query": f"site:{site} {query} reel",
                    "pageOptions": {"fetchPageContent": True},
                    "limit": 10,
                },
                timeout=30,
            )
            resp.raise_for_status()
            results = resp.json().get("data", [])
            clips = []
            for r in results:
                url = r.get("url", "")
                if "/reel/" not in url and "/status/" not in url:
                    continue
                content = r.get("markdown", "") or r.get("content", "")
                clips.append({
                    "url": url,
                    "platform": "instagram" if "instagram" in url else "x",
                    "views": None,
                    "duration_sec": None,
                    "caption": content[:500],
                    "speaker": _extract_speaker(content),
                    "topic": _extract_topic(content),
                    "format": _detect_format(content),
                    "posted_date": None,
                    "original_source": _extract_source(content),
                    "full_episode_link": "",
                    "interview_date": None,
                    "credits_handle": "",
                    "already_on_brainsbyai": "No",
                    "already_on_competitor": "No",
                })
            return clips
        except Exception as e:
            log.warning("Firecrawl search error [%s]: %s", query, e)
            return []

    # ── Public interface ─────────────────────────────────────────────────────

    async def audit_account(self, handle: str, platform: str) -> List[Dict]:
        await self._start_browser()
        try:
            if platform == "instagram":
                await self._instagram_login()
                return await self._instagram_audit_account(handle)
        except Exception as e:
            log.error("Account audit failed: %s", e)
        finally:
            await self._stop_browser()
        return []

    async def search(self, query: str, platform: str) -> List[Dict]:
        results = []
        await self._start_browser()
        try:
            if platform == "instagram":
                await self._instagram_login()
                results = await self._instagram_search(query)
                if not results and self.firecrawl_key:
                    log.info("  Playwright returned 0 — falling back to Firecrawl")
                    results = self._firecrawl_search(query, site="instagram.com")
            elif platform == "x":
                results = await self._x_search(query)
                if not results and self.firecrawl_key:
                    results = self._firecrawl_search(query, site="x.com")
        except Exception as e:
            log.error("Search failed [%s / %s]: %s", platform, query, e)
        finally:
            await self._stop_browser()
        return results


# ── Parsing helpers ───────────────────────────────────────────────────────────

def _parse_views(text: str) -> int:
    if not text:
        return 0
    text = text.replace(",", "").strip().upper()
    match = re.search(r"([\d.]+)\s*([KMB]?)", text)
    if not match:
        return 0
    num = float(match.group(1))
    suffix = match.group(2)
    if suffix == "K":
        return int(num * 1_000)
    if suffix == "M":
        return int(num * 1_000_000)
    if suffix == "B":
        return int(num * 1_000_000_000)
    return int(num)


def _parse_duration(text: str) -> Optional[int]:
    """Convert MM:SS or SS to seconds."""
    if not text:
        return None
    match = re.search(r"(\d+):(\d+)", text)
    if match:
        return int(match.group(1)) * 60 + int(match.group(2))
    match = re.search(r"(\d+)s", text)
    if match:
        return int(match.group(1))
    return None


KNOWN_SPEAKERS = [
    "Sam Altman", "Jensen Huang", "Elon Musk", "Mark Zuckerberg",
    "Sundar Pichai", "Satya Nadella", "Jeff Bezos", "Tim Cook",
    "Dario Amodei", "Ilya Sutskever", "Andrej Karpathy", "Yann LeCun",
    "Geoffrey Hinton", "Demis Hassabis", "Mustafa Suleyman", "Fei-Fei Li",
    "Andrew Ng", "Yoshua Bengio", "Gary Marcus", "Mo Gawdat",
    "Kai-Fu Lee", "Tristan Harris", "Ray Kurzweil", "Peter Thiel",
    "Aravind Srinivas", "Palmer Luckey", "Bill Gates", "Lex Fridman",
]

def _extract_speaker(text: str) -> str:
    for name in KNOWN_SPEAKERS:
        if name.lower() in text.lower():
            return name
    return ""

def _extract_topic(text: str) -> str:
    """Return first ~100 chars of caption as topic placeholder."""
    return text[:100].strip().replace("\n", " ") if text else ""

def _detect_format(text: str) -> str:
    text_lower = text.lower()
    for fmt in ["podcast", "interview", "keynote", "conference", "panel", "debate", "speech"]:
        if fmt in text_lower:
            return fmt
    return "interview"  # default assumption for clip-style content

def _extract_source(text: str) -> str:
    sources = [
        "Lex Fridman", "Joe Rogan", "Diary of a CEO", "All In",
        "Dwarkesh", "Huberman", "20VC", "CNBC", "Bloomberg", "BBC",
        "CNN", "TED", "Davos", "GTC", "Google I/O",
    ]
    for s in sources:
        if s.lower() in text.lower():
            return s
    return ""

def _extract_credits_handle(caption: str) -> str:
    """Pull @handle from caption for credit attribution."""
    match = re.search(r"@([\w.]+)", caption)
    return f"@{match.group(1)}" if match else ""
