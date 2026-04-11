"""
Deduplication Store
Tracks every clip URL ever found or posted so nothing repeats across daily runs.
"""

import json
import logging
import os
from datetime import datetime
from typing import List, Dict, Any

log = logging.getLogger(__name__)


class DeduplicationStore:
    def __init__(self, path: str):
        self.path = path
        self._data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                return json.load(f)
        return {
            "found_urls": [],        # every URL ever surfaced by any run
            "posted_urls": [],       # URLs already live on @brainsbyai
            "last_updated": None,
        }

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self._data["last_updated"] = datetime.utcnow().isoformat()
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)
        log.info("Dedup store saved — %d total known URLs", len(self._data["found_urls"]))

    def register_posted(self, clips: List[Dict]):
        """Mark clips already on @brainsbyai so they're never flagged as new."""
        urls = [c["url"] for c in clips if c.get("url")]
        added = 0
        for url in urls:
            if url not in self._data["posted_urls"]:
                self._data["posted_urls"].append(url)
                added += 1
            if url not in self._data["found_urls"]:
                self._data["found_urls"].append(url)
        log.info("  Registered %d @brainsbyai posted URLs", added)

    def filter_new(self, clips: List[Dict]) -> List[Dict]:
        """Return only clips whose URL has never been seen before."""
        known = set(self._data["found_urls"] + self._data["posted_urls"])
        fresh = []
        seen_this_run = set()
        for clip in clips:
            url = clip.get("url", "")
            if not url:
                continue
            if url in known or url in seen_this_run:
                continue
            seen_this_run.add(url)
            fresh.append(clip)
        return fresh

    def mark_found(self, clips: List[Dict]):
        """Add newly surfaced clip URLs to the store."""
        for clip in clips:
            url = clip.get("url", "")
            if url and url not in self._data["found_urls"]:
                self._data["found_urls"].append(url)
