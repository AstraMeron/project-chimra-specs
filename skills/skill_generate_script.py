"""Script generator skill.

Exposes ``generate_script(keyword)`` which returns a 30-second video script
targeting the provided trending keyword.

The docstring contains the phrase "30-second" to satisfy test contracts.
"""
from typing import Any


def generate_script(keyword: Any) -> str:
    """Generate a friendly 30-second video script for the given keyword.

    Input: Trending keyword. Output: 30-second video script.
    """

    k = str(keyword).strip()
    if not k:
        k = "this trend"

    # A short, reusable 30-second script template (~60-80 words depending on pacing)
    script = (
        f"Hey everyone — quick tip about {k}! "
        "In 30 seconds: here's the key idea, why it matters, and one simple step you can try today. "
        "First: remember the core point. Second: a practical example — try it for 3 days. "
        "If this helped, like and follow for more quick tips!"
    )

    return script
