import pytest

# Based on research/architecture_strategy.md: the Judge Agent is a quality gate
# that ensures content aligns with the project's "DNA" (SOUL). This test
# asserts that content which clearly does NOT match the SOUL should be
# rejected by the Judge Agent. The implementation is intentionally missing
# so this test should fail until the Judge Agent is implemented.


def test_judge_rejects_content_not_matching_soul():
    # Example SOUL DNA (minimal representation for the test)
    soul = {
        "tone": "formal",
        "topics": ["health", "fitness"],
        "safety": {"allow_financial": False},
    }

    # Content that clearly conflicts with the SOUL
    content = {
        "text": "Buy crypto now! Quick money with no risk.",
        "tone": "casual",
        "topics": ["finance"],
    }

    # We expect a module `agents.judge` with `evaluate(content, soul)` that
    # returns a dict like {"approved": bool, "reason": str}.
    from agents.judge import evaluate

    result = evaluate(content, soul)

    assert isinstance(result, dict)
    assert result.get("approved") is False
    assert "mismatch" in (result.get("reason") or "").lower()
