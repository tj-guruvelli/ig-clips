"""
IG Clips Daily Discovery Engine
Finds viral AI podcast/interview clips and deduplicates across runs.
"""

import asyncio
import logging
import os
from datetime import datetime

from dedup import DeduplicationStore
from scraper import ClipScraper
from qualifier import qualify_clip
from output import save_output

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
log = logging.getLogger(__name__)


# ── Search config drawn from your original prompt ──────────────────────────
TIER1_SPEAKERS = [
    "Sam Altman", "Jensen Huang", "Elon Musk", "Mark Zuckerberg",
    "Sundar Pichai", "Satya Nadella", "Jeff Bezos", "Tim Cook",
    "Larry Ellison", "Marc Andreessen",
]

TIER2_SPEAKERS = [
    "Dario Amodei", "Ilya Sutskever", "Andrej Karpathy", "Yann LeCun",
    "Geoffrey Hinton", "Demis Hassabis", "Mustafa Suleyman", "Fei-Fei Li",
    "Andrew Ng", "Yoshua Bengio", "Gary Marcus", "Stuart Russell",
]

TIER3_SPEAKERS = [
    "Raoul Pal", "Mo Gawdat", "Kai-Fu Lee", "Tristan Harris", "Ray Kurzweil",
    "Peter Thiel", "Aravind Srinivas", "Palmer Luckey", "Bill Gates",
]

PODCAST_SOURCES = [
    "Lex Fridman", "Joe Rogan", "Diary of a CEO", "All In Podcast",
    "Dwarkesh Podcast", "Huberman Lab AI", "20VC", "Acquired podcast AI",
]

TOPIC_SEARCHES = [
    "AI AGI future", "AI takes jobs", "AI warning 2025",
    "AI beats human", "AI dangerous", "ChatGPT interview",
    "humanoid robot", "AI regulation Senate", "AI prediction 2025",
    "large language model interview", "AI agents future",
]

INDUSTRY_SEARCHES = [
    "AI replaces lawyers", "AI doctor diagnosis", "AI trading hedge fund",
    "AI replaces teachers", "AI music film", "Tesla Optimus robot",
    "AI weapons warfare", "AI Davos World Economic Forum",
    "self-driving AI interview", "AI drug discovery",
]

THEAIBOLT_HANDLE = "theaibolt"

PLATFORMS = ["instagram", "x"]  # x = Twitter/X


async def run():
    log.info("=== IG Clips Daily Run — %s ===", datetime.now().strftime("%Y-%m-%d"))

    store = DeduplicationStore("data/found_clips.json")
    store.increment_run()
    scraper = ClipScraper(
        instagram_user=os.getenv("INSTAGRAM_USERNAME"),
        instagram_pass=os.getenv("INSTAGRAM_PASSWORD"),
        firecrawl_key=os.getenv("FIRECRAWL_API_KEY"),
    )

    # ── GUARD 1: no scraping backend => fail fast, never report a fake success.
    if not scraper.firecrawl_key and not (scraper.instagram_user and scraper.instagram_pass):
        raise SystemExit(
            "FATAL: no scraping backend configured. Set FIRECRAWL_API_KEY (or "
            "INSTAGRAM_USERNAME + INSTAGRAM_PASSWORD). Refusing to run 0-source and "
            "report an empty 'success' (this hid 97 green-but-empty runs for months)."
        )

    # Step 1 — pull @theaibolt already-posted content
    log.info("Step 1: Auditing @theaibolt for already-posted clips...")
    already_posted = await scraper.audit_account(THEAIBOLT_HANDLE, platform="instagram")
    store.register_posted(already_posted)
    log.info("  Found %d clips already posted on @theaibolt", len(already_posted))

    # Step 2+3 — search across platforms
    all_candidates = []

    search_queries = (
        [f"{s} AI interview" for s in TIER1_SPEAKERS] +
        [f"{s} podcast clip" for s in TIER2_SPEAKERS] +
        [f"{s} AI interview" for s in TIER3_SPEAKERS] +
        [f"{p} clip" for p in PODCAST_SOURCES] +
        TOPIC_SEARCHES +
        INDUSTRY_SEARCHES
    )

    for platform in PLATFORMS:
        log.info("Searching platform: %s (%d queries)", platform, len(search_queries))
        for query in search_queries:
            candidates = await scraper.search(query=query, platform=platform)
            all_candidates.extend(candidates)

    log.info("Total raw candidates found: %d", len(all_candidates))

    # ── GUARD 2: 0 raw candidates from a FULL sweep is a broken/blocked scrape
    # integration (bad key, 4xx, quota, or IP block), NOT a legitimate quiet day —
    # a working scrape always returns *some* candidates even if all are dupes or
    # unqualified. Fail LOUD (non-zero exit) so the run goes RED instead of
    # silently reporting an empty success. This is the exact bug that let a broken
    # Firecrawl integration pass 97 "successful" runs while sourcing 0 clips.
    if not all_candidates:
        store.save()  # persist the run counter, then fail
        raise SystemExit(
            f"FATAL: 0 raw candidates from {len(search_queries) * len(PLATFORMS)} "
            f"searches across {PLATFORMS}. This is a SCRAPE INTEGRATION FAILURE "
            f"(broken API key, 4xx/quota, or blocked), not an empty result. "
            f"Failing the run so it is visible. Check the scraper backend."
        )

    # Step 4 — deduplicate
    fresh = store.filter_new(all_candidates)
    log.info("After dedup: %d fresh candidates", len(fresh))

    # Step 5 — qualify each clip
    qualified = []
    for clip in fresh:
        result = qualify_clip(clip)
        if result["passes"]:
            qualified.append(result["clip"])
        else:
            log.debug("  SKIP [%s] — %s", clip.get("url", "?"), result["reason"])

    log.info("Qualified clips: %d", len(qualified))

    # Step 6 — save output and update dedup store
    if qualified:
        output_path = save_output(qualified, output_dir="output")
        store.mark_found(qualified)
        store.save()
        log.info("Output saved → %s", output_path)
    else:
        store.save()
        log.info("No new qualifying clips found today.")

    # Step 7 — report tracking stats and available source library
    stats = store.get_stats()
    log.info("=== Tracking Stats ===")
    log.info("  Runs: %d | Total found: %d | Qualified: %d | Posted: %d",
             stats["runs"], stats["total_found"], stats["total_qualified"], stats["total_posted"])
    log.info("  1M+ view sources: %d total | %d available (not yet posted)",
             stats["total_over_1m"], stats["available_1m_sources"])

    source_library = store.get_source_library()
    if source_library:
        log.info("=== Top Available Source Clips (1M+ views, not yet posted) ===")
        for clip in source_library[:10]:
            log.info("  %s | %s views | %s | %s",
                     clip.get("url", "?"),
                     f"{clip.get('views', 0):,}",
                     clip.get("speaker", "Unknown"),
                     clip.get("source", "Unknown source"))

    log.info("=== Run complete ===")


if __name__ == "__main__":
    asyncio.run(run())
