"""
Output Formatter
Saves qualifying clips as a CSV report for easy review.
Generates hook options using Claude API.
"""

import csv
import os
import json
import logging
from datetime import datetime
from typing import List, Dict, Any

import requests

log = logging.getLogger(__name__)

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
CLAUDE_MODEL = "claude-sonnet-4-20250514"


def generate_hooks(clip: Dict[str, Any]) -> List[str]:
    """
    Use Claude API to generate 3 hook variations per clip.
    Falls back to placeholder strings if API call fails.
    """
    speaker = clip.get("speaker", "Unknown speaker")
    topic = clip.get("topic", "AI")
    pillar = ", ".join(clip.get("content_pillars", ["educational"]))

    prompt = f"""Generate exactly 3 Instagram reel hook options for this AI clip.

Speaker: {speaker}
Topic: {topic}
Content pillar: {pillar}

Rules (strictly follow all):
- Under 8 words each
- Grade 5 reading level
- No em dashes
- No colons before speaker names
- No brain emoji on opening line
- Never resolve the curiosity gap in the hook itself
- Formula: Subject named + tension created + resolution withheld

Return ONLY a JSON array of 3 strings, no other text:
["hook 1", "hook 2", "hook 3"]"""

    try:
        resp = requests.post(
            ANTHROPIC_API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": CLAUDE_MODEL,
                "max_tokens": 200,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=20,
        )
        resp.raise_for_status()
        text = resp.json()["content"][0]["text"].strip()
        hooks = json.loads(text)
        return hooks if isinstance(hooks, list) else ["[Hook generation failed]"] * 3
    except Exception as e:
        log.warning("Hook generation failed for %s: %s", clip.get("url"), e)
        return [
            f"{speaker} just changed everything about AI",
            f"Nobody tells you this about {topic}",
            f"{speaker} said what everyone was thinking",
        ]


FIELDNAMES = [
    "clip_number",
    "platform",
    "url",
    "views",
    "date_posted",
    "speaker",
    "topic",
    "duration_sec",
    "content_pillars",
    "original_source",
    "full_episode_link",
    "interview_date",
    "credits_handle",
    "already_on_brainsbyai",
    "already_on_competitor",
    "hook_1",
    "hook_2",
    "hook_3",
    "low_views_flag",
    "pillar_unverified",
]


def save_output(clips: List[Dict[str, Any]], output_dir: str = "output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(output_dir, f"clips_{date_str}.csv")

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES, extrasaction="ignore")
        writer.writeheader()

        for i, clip in enumerate(clips, start=1):
            log.info("  Generating hooks for clip %d/%d...", i, len(clips))
            hooks = generate_hooks(clip)

            pillars = clip.get("content_pillars", [])
            if isinstance(pillars, list):
                pillars = ", ".join(pillars)

            row = {
                "clip_number": i,
                "platform": clip.get("platform", ""),
                "url": clip.get("url", ""),
                "views": clip.get("views", ""),
                "date_posted": clip.get("posted_date", ""),
                "speaker": clip.get("speaker", ""),
                "topic": clip.get("topic", ""),
                "duration_sec": clip.get("duration_sec", ""),
                "content_pillars": pillars,
                "original_source": clip.get("original_source", "UNCONFIRMED"),
                "full_episode_link": clip.get("full_episode_link", ""),
                "interview_date": clip.get("interview_date", ""),
                "credits_handle": clip.get("credits_handle", ""),
                "already_on_brainsbyai": clip.get("already_on_brainsbyai", "No"),
                "already_on_competitor": clip.get("already_on_competitor", "No"),
                "hook_1": hooks[0] if len(hooks) > 0 else "",
                "hook_2": hooks[1] if len(hooks) > 1 else "",
                "hook_3": hooks[2] if len(hooks) > 2 else "",
                "low_views_flag": "⚠️" if clip.get("low_views_flag") else "",
                "pillar_unverified": "⚠️" if clip.get("pillar_unverified") else "",
            }
            writer.writerow(row)

    log.info("Saved %d clips → %s", len(clips), path)
    return path
