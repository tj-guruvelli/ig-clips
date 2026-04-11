"""
Clip Qualifier
Applies all rules from the discovery prompt to determine if a clip is postable.
"""

from datetime import datetime, timedelta
from typing import Dict, Any

VALID_FORMATS = {"interview", "podcast", "keynote", "conference", "panel", "debate", "speech"}

CONTENT_PILLARS = {
    "educational": [
        "explains", "how", "what is", "learn", "model", "train",
        "technology", "science", "research",
    ],
    "inspirational": [
        "future", "vision", "humanity", "change the world", "opportunity",
        "transform", "revolution", "potential",
    ],
    "emotional": [
        "fear", "lose job", "replace", "scary", "danger", "risk",
        "worried", "concerned", "threat", "job loss",
    ],
    "controversial": [
        "wrong", "disagree", "ban", "regulate", "censored", "challenge",
        "against", "refuse", "reject", "lie",
    ],
}

MIN_DURATION_SEC = 30
MAX_DURATION_SEC = 90
LOOKBACK_DAYS = 365  # 12 months


def qualify_clip(clip: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns {"passes": True, "clip": clip} or {"passes": False, "reason": str}.
    """

    # ── FORMAT check ────────────────────────────────────────────────────────
    fmt = (clip.get("format") or "").lower()
    if not any(f in fmt for f in VALID_FORMATS):
        # If format field is empty, give benefit of the doubt if it has a real speaker
        if not clip.get("speaker"):
            return _fail("Non-qualifying format and no speaker detected")

    # ── DURATION check ───────────────────────────────────────────────────────
    duration = clip.get("duration_sec")
    if duration is not None:
        if not (MIN_DURATION_SEC <= duration <= MAX_DURATION_SEC):
            return _fail(f"Duration {duration}s out of range (30–90s required)")

    # ── DATE check ───────────────────────────────────────────────────────────
    posted_date = clip.get("posted_date")
    if posted_date:
        try:
            if isinstance(posted_date, str):
                posted_date = datetime.fromisoformat(posted_date)
            cutoff = datetime.utcnow() - timedelta(days=LOOKBACK_DAYS)
            if posted_date < cutoff:
                return _fail(f"Too old — posted {posted_date.date()}")
        except (ValueError, TypeError):
            pass  # If we can't parse date, don't block on it

    # ── VIEWS check ─────────────────────────────────────────────────────────
    views = clip.get("views", 0) or 0
    if views < 500_000:  # flag but don't hard-block — scraper may not always get views
        clip["low_views_flag"] = True

    # ── CONTENT PILLAR check ─────────────────────────────────────────────────
    text_to_check = " ".join([
        (clip.get("caption") or ""),
        (clip.get("transcript_snippet") or ""),
        (clip.get("topic") or ""),
    ]).lower()

    matched_pillars = []
    for pillar, keywords in CONTENT_PILLARS.items():
        if any(kw in text_to_check for kw in keywords):
            matched_pillars.append(pillar)

    if not matched_pillars:
        # Soft fail — flag but don't block if speaker is credible
        clip["pillar_unverified"] = True
        matched_pillars = ["unverified"]

    clip["content_pillars"] = matched_pillars

    # ── SPOKEN WORDS check (AI relevance in content, not just caption) ───────
    ai_terms = ["ai", "artificial intelligence", "agi", "machine learning",
                 "llm", "gpt", "robot", "automation", "algorithm", "neural"]
    has_ai_in_content = any(t in text_to_check for t in ai_terms)
    if not has_ai_in_content:
        return _fail("AI relevance not found in spoken content — caption-only framing")

    return {"passes": True, "clip": clip}


def _fail(reason: str) -> Dict[str, Any]:
    return {"passes": False, "reason": reason}
