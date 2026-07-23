# IG Clips — Daily Viral AI Clip Discovery

Finds viral (**1M+ view**) AI podcast/interview clips on Instagram and keeps a rolling backlog of ready-to-pick candidates for the **@theaiaxon** account. Deduplicates across runs so nothing is surfaced twice.

---

## Architecture (current — updated 2026-07-22)

**Primary: a claude.ai cloud routine** ("IG clips routine", daily ~5 AM CDT). A scheduled Claude agent that:
1. Scrapes competitor theme-pages via the **Apify** connector (`apify/instagram-reel-scraper`) — returns reels with real `videoPlayCount` / duration / caption.
2. Filters to ≥1,000,000 plays + the qualifying rules below, dedups vs `data/found_clips.json` + `data/backlog.json`.
3. Maintains a pool of up to **100** candidates in `data/backlog.json`; alerts at 90.
4. Commits + pushes `data/` back to this repo (a fresh clone loses everything otherwise).

It uses **MCP connectors** (Apify, Metricool, Composio) — **no API keys are stored in this repo**.

**Legacy: GitHub Actions** (`.github/workflows/daily.yml`) — **DISABLED 2026-07-22**. It ran the local Python engine (Firecrawl web-search + Playwright IG login), which returned **0 clips** for months: Firecrawl 400'd every query and web-search has no IG view counts. Superseded by the cloud routine + Apify.

**Local fallback: `src/main.py`** — the Python engine. Firecrawl request updated to the v2 API and kept as a general-web scraper. Now **fails loud** (non-zero exit) if no scrape backend is configured or a full sweep returns 0 raw candidates, so a broken integration goes RED instead of a silent empty "success".

---

## Accounts

- **@theaiaxon** — the posting target (fresh account, growth 0→10k). Dedup is against *its* posted history.
- **@theaibolt** — source catalog + speaker-saturation signal (its ~143 posts are proven picks to resurface).
- `@brainsbyai` was the original name for this project; retired — do not use.

## Data files

- `data/found_clips.json` — dedup store: `found_urls` (everything ever surfaced) + `posted_urls` (@theaibolt history) + `clips_log` (surfaced 1M+ clips).
- `data/backlog.json` — the maintained pool of ready-to-pick candidates + status.
- `data/DISCOVERY-LOG.md` — dated run reports.

## Qualifying criteria

1M+ views (hard gate) · real person speaking (interview/podcast/keynote — exclude AI-generated video, memes, faceless voiceover) · genuinely about AI in the spoken words · not already posted · prefer 30–90s · prefer last 12 months.

---

## Keys & secrets

The cloud routine needs **no keys in this repo** — it authenticates through the attached MCP connectors.

If you re-enable the GitHub Actions path, store keys as **encrypted Secrets** (Settings → Secrets and variables → Actions → **Secrets** tab) — **never as plaintext Variables**. Actions *Variables* are unencrypted and printed in logs; API keys placed there are exposed. (Any keys currently sitting in the *Variables* tab should be deleted and rotated.)

## Local run

```bash
pip install -r requirements.txt
# put FIRECRAWL_API_KEY (or APIFY_API_KEY), optional IG creds, in .env
cd src && python main.py
```

Fails fast if no scrape backend is set, and fails loud if a full search sweep finds 0 candidates (broken/blocked integration, not an empty result).
