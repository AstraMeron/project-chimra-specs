```markdown
# ADR 0001 — Use NoSQL (MongoDB) for Polymorphic Agent & Artifact Data

## Context
Project Chimera exchanges heterogeneous artifacts (video metadata, short text artifacts, monetization blobs, raw provider JSON) between multiple agent types. The `Artifact` envelope is polymorphic and can grow with additional fields depending on platform and analyzer signals. The system also requires append-only processing history and flexible agent_signals.

## Decision
We will standardize on a NoSQL document store (MongoDB 6.x+) for the primary `videos` collection that stores ingested artifacts and their processing history.

## Rationale
- **Flexible Schema:** MongoDB stores polymorphic documents without costly schema migrations, allowing `raw_payload`, `extracted_features`, and `monetization` to evolve independently per platform.
- **Append-only History:** `processing_history` as an array suits MongoDB's document model; it can be appended atomically and indexed for queries.
- **Indexing & Performance:** We can add targeted indexes (`sourcePlatform+externalId`, `agent_signals.confidence`, `agent_signals.topics`) to optimize common Judge and HITL queries.
- **Operational Maturity:** MongoDB is a mature, hosted-friendly option that integrates with cloud providers and supports change streams for event-driven MCP logging.
- **Document-level Transactions:** For the few operations requiring atomicity across multiple collections (e.g., archive + create event), MongoDB supports multi-document transactions.

## Alternatives Considered
- **Relational DB (Postgres):** Strong for structured data and joins, but requires frequent migrations and polymorphic fields (JSONB) complicate querying and indexing patterns for large-scale time-series artifacts.
- **Wide-column stores (Cassandra):** Good for high write rates but lacks the flexible document model and ad-hoc querying convenience we need for audit and inspection workflows.

## Implications
- **Schema Governance:** While schema-less, we define recommended document shapes in `specs/technical.md` and rely on validators and index policies to prevent drift.
- **Archival Strategy:** Large `processing_history` arrays should be truncated and moved to `video_events` collection to keep primary documents lean.
- **Backups & Compliance:** Regular backups and retention policies must be in place to satisfy auditability requirements.

## Decision Status
Accepted — MongoDB (NoSQL document store) for polymorphic artifact storage and audit trails.

``` 
