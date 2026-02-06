```markdown
# Project Chimera — Governance

This document summarizes our Branching Strategy and Security Formality tied to the project's autonomy guarantees (notably the $10 financial safety limit and HITL thresholds).

## Branching Strategy
- **Protected `main`**: `main` is protected by branch rules. Direct pushes are disallowed; all changes must be via pull request that pass CI and automated checks.
- **`develop` for Integration**: Optional integration branch for cross-feature testing. Not required for small teams.
- **Feature Branches (`feature/*`)**: Short-lived branches for development. Branch names should reference a spec or ticket (e.g. `feature/spec-123-add-judge-audit`).
- **Release / Hotfix (`release/*`, `hotfix/*`)**: Used to stage releases and fix critical issues on `main`.
- **Pull Request Requirements**: PRs targeting `main` or `develop` must reference the relevant `specs/` document(s), include tests, pass CI, and require at least one approver.

## Security Formality
Security formalities are enforced to protect the system and the economic boundaries enforced by the Judge logic.

### Protecting the $10 Limit
- **Judge-level Enforcement:** The Judge implements a hard gate: any candidate containing financial topics or an explicit `amount` above $10 will be flagged and denied automatic execution.
- **Approver Role:** Human Approvers are the only actors authorized to override the $10 threshold. Approver actions require authenticated SSO accounts + MFA and are recorded in the audit trail with identity, timestamp, and reason.
- **Auditability:** All decisions (Judge and human) are logged to the MCP audit store and persisted in the `videos` collection or `video_events` archive with `plan_id`, `candidate_id`, `judge_id`, `human_reviewer_id`, and `proofOfAlignment`.
- **CI & Checks:** CI enforces tests that exercise safety logic; security scanners flag dangerous changes (e.g., code paths that would bypass Judge checks).

### HITL & Approvals
- **Tiered Human Review:** The 3-Tier HITL logic (>=95% auto, 85–95% assisted, <85% manual) is a de facto policy. UI workflows require that assisted/manual items be surfaced in the Governance Dashboard for human action.
- **RBAC & Least Privilege:** Approver accounts are restricted to the minimum set of privileges required to sign off on transactions; secrets and wallet keys are stored in a secrets manager.

## Operational Notes
- **Incident Response:** Any override of the Judge policy triggers a ticket and retrospective review by governance.
- **Data Retention:** Audit logs are retained per compliance policy; large histories may be archived to `video_events` to keep primary documents performant.

``` 
