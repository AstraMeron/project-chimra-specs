"""Safety check skill.

Exposes ``check_safety(script)`` which returns a numeric Safety Score
in the range 0-100.

Safety Score: a simple heuristic score where 100 is maximally safe and
0 is unsafe. The function is intentionally conservative: scripts that
mention prescriptions, investments, or direct calls-to-action to "buy"
will see their safety score reduced.
"""
from typing import Union


def check_safety(script: str) -> Union[int, float]:
    """Check the provided script and return a Safety Score (0-100).

    Safety Score is returned as a numeric value where higher means safer.
    This function performs lightweight keyword heuristics and length
    checks suitable for unit tests and TDD scaffolding.
    """

    if not script:
        return 0

    text = script.lower()
    score = 100

    # Penalize short/empty scripts
    if len(text.strip()) < 20:
        score -= 40

    # Sensitive keywords that reduce safety
    penalties = {
        "prescription": 40,
        "diagnose": 30,
        "medicine": 30,
        "prescribe": 40,
        "invest": 35,
        "investment": 35,
        "buy": 20,
        "crypto": 40,
        "loan": 30,
    }

    for kw, p in penalties.items():
        if kw in text:
            score -= p

    # Bound score
    score = max(0, min(100, score))
    return score
