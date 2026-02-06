"""Trend fetcher skill.

Exposes ``fetch_trends(platform)`` which returns a list of viral keywords.

Input: Platform (X/TikTok). Output: List of viral keywords.
"""
from typing import List


def fetch_trends(platform: str) -> List[str]:
    """Fetch a short list of trending keywords for the specified Platform.

    The `platform` argument is a string such as "X" or "TikTok". This
    implementation is a lightweight stub suitable for tests and TDD.
    """

    if not platform:
        return []

    p = platform.strip().lower()
    # Simple deterministic stubs per platform
    if p in ("x", "twitter"):
        return ["shortform", "viral_challenge", "lifehack"]
    if p in ("tiktok",):
        return ["dance_trend", "quick_recipe", "60sec_challenge"]

    # Generic fallback
    return ["trend1", "trend2", "trend3"]
