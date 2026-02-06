```markdown
# Governance Dashboard — HITL (Human-in-the-Loop)

## Purpose
The Governance Dashboard is the operational UI for human reviewers, auditors, and operators to inspect, triage, and approve candidate content that the Judge has flagged for human oversight. It provides an auditable workflow aligned with the project's 3-Tier HITL safety logic and SOUL DNA.

## Users & Roles
- **Reviewer:** Performs assisted reviews (Tier 2) and can approve or request changes.
- **Approver:** Authorized to provide manual sign-off (Tier 3) for financial actions > $10.
- **Auditor:** Views full audit trails and governance metrics; cannot mutate records.

## Key Screens

### 1) Queue Overview
- Filters: `plan_id`, `candidate_id`, `confidence_range`, `topic_tags`, `source_agent`, `time_range`.
- Columns: `candidate_id`, `summary`, `confidence`, `topics`, `judge_reason`, `received_at`, `tier`.
- Actions: `Inspect`, `Assign`, `Escalate`, `Dismiss`.

### 2) Candidate Detail / Inspection
- Header: `candidate_id`, `plan_id`, `source_agent`, `composer_confidence`, `judge_confidence`.
- Payload viewer: raw `Artifact` JSON-LD envelope and rendered content preview (text/video thumbnail).
- Evidence panel: `proofOfAlignment`, contributing signals (trend_score, source_agent confidence), and SOUL fingerprint.
- Action buttons: `Approve (auto/assisted)`, `Request Modification`, `Reject`, `Escalate to Approver`.
- Comment box: reviewers must provide a short `reason` when rejecting or escalating.

### 3) Financial Review Modal
- Presented when `monetization` is present or the Judge flagged `amount > $10`.
- Displays transaction summary, amount, destination (if any), and required approval checklist.
- Requires an `Approver` role to sign off; logs approver identity, timestamp, and proof of review.

### 4) Audit & History
- Immutable timeline for each `candidate_id`: Judge decision, reviewer actions, human approver signatures, and downstream Executor actions.
- Exportable records (JSON/CSV) and API hooks for MCP logging and compliance ingestion.

## Policies Embedded in UI
- **Decision Evidence Required:** All manual approvals must include a human `reason` and reference the SOUL fingerprint.
- **Escalation Rules:** Repeated failures from the same Planner/Creator auto-quarantine outputs and notify governance.
- **Retention:** Audit trails are append-only; older entries can be archived to a `video_events` collection.

## Accessibility & Security
- Role-based access control (RBAC) integrating with org SSO and device-level MFA for Approvers.
- Data minimization in previews (redact PII by default) and read-only auditor modes.

## Metrics & Dashboards
- HITL latency (time to human decision), approval rates by topic, repeated failure counts per agent, and financial request volume.

## Integration Points
- MCP logging API for writing audit records.
- Judge and Planner webhooks for real-time queueing.
- MongoDB (videos collection) for artifact storage and `video_events` for historical events.

``` 
