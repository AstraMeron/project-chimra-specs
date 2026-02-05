def test_fetch_trends_interface():
    # TDD baseline: expects a module `skills.skill_fetch_trends` exposing `fetch_trends`
    from skills.skill_fetch_trends import fetch_trends

    assert callable(fetch_trends)
    # contract: Input: Platform (X/TikTok). Output: List of viral keywords.
    assert "Platform" in (fetch_trends.__doc__ or "")
