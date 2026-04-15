"""
Deduplication Store
Tracks every clip URL ever found or posted so nothing repeats across daily runs.
Maintains a rich metadata log for clips with 1M+ views as a source library.
"""

import json
import logging
import os
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

log = logging.getLogger(__name__)

VIEW_THRESHOLD = 1_000_000


class DeduplicationStore:
    def __init__(self, path: str):
        self.path = path
        self._data: Dict[str, Any] = self._load()

    def _load(self) -> Dict[str, Any]:
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                data = json.load(f)
            # Migrate legacy format: add new fields if missing
            if "clips_log" not in data:
                data["clips_log"] = {}
            if "stats" not in data:
                data["stats"] = {
                    "total_found": len(data.get("found_urls", [])),
                    "total_qualified": 0,
                    "total_over_1m": 0,
                    "runs": 0,
                }
            return data
        return {
            "found_urls": [],
            "posted_urls": [],
            "clips_log": {},
            "stats": {
                "total_found": 0,
                "total_qualified": 0,
                "total_over_1m": 0,
                "runs": 0,
            },
            "last_updated": None,
        }

    def save(self) -> None:
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        self._data["last_updated"] = datetime.now(timezone.utc).isoformat()
        with open(self.path, "w") as f:
            json.dump(self._data, f, indent=2)
        stats = self._data["stats"]
        log.info(
            "Dedup store saved — %d total URLs, %d in source library (1M+ views), %d qualified",
            len(self._data["found_urls"]),
            stats["total_over_1m"],
            stats["total_qualified"],
        )

    def register_posted(self, clips: List[Dict]) -> None:
        """Mark clips already on @theaibolt so they're never flagged as new."""
        urls = [c["url"] for c in clips if c.get("url")]
        added = 0
        for url in urls:
            if url not in self._data["posted_urls"]:
                self._data["posted_urls"].append(url)
                added += 1
            if url not in self._data["found_urls"]:
                self._data["found_urls"].append(url)
            # Log posted clips so we know what content has already been used
            self._upsert_clip_log(url, {"status": "posted"})
        log.info("  Registered %d @theaibolt posted URLs", added)

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

    def mark_found(self, clips: List[Dict]) -> None:
        """Add newly surfaced clip URLs to the store with full metadata."""
        for clip in clips:
            url = clip.get("url", "")
            if not url:
                continue
            if url not in self._data["found_urls"]:
                self._data["found_urls"].append(url)
                self._data["stats"]["total_found"] += 1

            views = clip.get("views") or 0
            is_over_1m = views >= VIEW_THRESHOLD

            self._upsert_clip_log(url, {
                "platform": clip.get("platform", ""),
                "views": views,
                "speaker": clip.get("speaker", ""),
                "source": clip.get("original_source", ""),
                "topic": clip.get("topic", ""),
                "format": clip.get("format", ""),
                "content_pillars": clip.get("content_pillars", []),
                "duration_sec": clip.get("duration_sec"),
                "credits_handle": clip.get("credits_handle", ""),
                "status": "qualified",
                "over_1m_views": is_over_1m,
            })

            self._data["stats"]["total_qualified"] += 1
            if is_over_1m:
                self._data["stats"]["total_over_1m"] += 1

    def increment_run(self) -> None:
        """Increment the run counter for tracking."""
        self._data["stats"]["runs"] += 1

    def get_source_library(self) -> List[Dict]:
        """Return all tracked clips with 1M+ views that haven't been posted yet.
        This is the 'never run out of content' queue."""
        posted = set(self._data["posted_urls"])
        sources = []
        for url, meta in self._data["clips_log"].items():
            if meta.get("over_1m_views") and url not in posted:
                sources.append({"url": url, **meta})
        sources.sort(key=lambda c: c.get("views", 0), reverse=True)
        return sources

    def get_stats(self) -> Dict[str, Any]:
        """Return tracking stats for logging."""
        posted = set(self._data["posted_urls"])
        available = sum(
            1 for url, meta in self._data["clips_log"].items()
            if meta.get("over_1m_views") and url not in posted
        )
        return {
            **self._data["stats"],
            "available_1m_sources": available,
            "total_posted": len(self._data["posted_urls"]),
        }

    def _upsert_clip_log(self, url: str, updates: Dict[str, Any]) -> None:
        """Insert or update a clip in the metadata log."""
        existing = self._data["clips_log"].get(url, {})
        if "first_found" not in existing:
            existing["first_found"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        existing["last_seen"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        # Only update views if the new value is higher (views grow over time)
        if updates.get("views", 0) > existing.get("views", 0):
            existing["views"] = updates["views"]
        # Merge all other fields
        for key, val in updates.items():
            if key != "views" and val:
                existing[key] = val
        self._data["clips_log"][url] = existing
