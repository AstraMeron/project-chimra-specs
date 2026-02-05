def test_check_safety_interface():
    # TDD baseline: expects a module `skills.skill_check_safety` exposing `check_safety`
    from skills.skill_check_safety import check_safety

    assert callable(check_safety)
    # contract: Input: Generated script. Output: Safety Score (0-100).
    assert "Safety Score" in (check_safety.__doc__ or "")
