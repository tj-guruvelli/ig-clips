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

BRAINSBYAI_HANDLE = "brainsbyai"

PLATFORMS = ["instagram", "x"]  # x = Twitter/X


async def run():
    log.info("=== IG Clips Daily Run — %s ===", datetime.now().strftime("%Y-%m-%d"))

    store = DeduplicationStore("data/found_clips.json")
    scraper = ClipScraper(
        instagram_user=os.getenv("INSTAGRAM_USERNAME"),
        instagram_pass=os.getenv("INSTAGRAM_PASSWORD"),
        firecrawl_key=os.getenv("FIRECRAWL_API_KEY"),
    )

    # Step 1 — pull @brainsbyai already-posted content
    log.info("Step 1: Auditing @brainsbyai for already-posted clips...")
    already_posted = await scraper.audit_account(BRAINSBYAI_HANDLE, platform="instagram")
    store.register_posted(already_posted)
    log.info("  Found %d clips already posted on @brainsbyai", len(already_posted))

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
        log.info("No new qualifying clips found today.")

    log.info("=== Run complete ===")


if __name__ == "__main__":
    asyncio.run(run())
