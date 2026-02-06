# Project Chimera: The Orchestrator's Factory

## Status
- **TDD Baseline:** PASSING
- **CI/CD:** Active (GitHub Actions)

## Governance Logic (Summary)
- **$10 Safety Limit:** Any candidate content that triggers a financial action with an amount greater than $10 is blocked from automatic execution and requires explicit human approval.
- **HITL Confidence Thresholds:** Judge enforces three tiers based on confidence score (0-100):
	- >= 95% — Autonomous (auto-execute for non-financial content)
	- 85%–94.99% — Assisted Review (queue for fast human check)
	- < 85% — Manual Approval required

## Agent Capabilities
- **Judge:** Evaluates candidate artifacts against the SOUL DNA and governance rules, returns approval, confidence, reason, and actions.
- **Trend Fetcher:** `skills.skill_fetch_trends` — returns platform-specific trending keywords.
- **Script Generator:** `skills.skill_generate_script` — creates short (30-second) video scripts from keywords.
- **Safety Gate:** `skills.skill_check_safety` — computes a Safety Score (0-100) for generated content.

## Quick Start
1. Create and activate your virtual environment and install development dependencies.
2. Ensure the project root is on `PYTHONPATH` and run tests with `uv`:

```powershell
$env:PYTHONPATH = '.'
uv run pytest
```

## Notes
- All agent interfaces and enforcement rules are defined in `specs/functional.md` and `specs/technical.md`.
- See `CLAUDE.md` for the Prime Directive and development constraints.
