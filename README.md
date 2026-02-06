# Project Chimera: A Sovereign Agent Node

### "The Evolution from SaaS to Service-as-Software"

Project Chimera is an exploration into the next frontier of the agentic web. We are witnessing a fundamental paradigm shift: moving from **SaaS (Software as a Service)**—where humans use tools to work—to **Service *as* Software**, where autonomous agents *are* the workers.

Chimera is a **Sovereign Agent Node**. It is not just a bot; it is a digital entity with its own identity, a governing constitution, and the ability to engage in independent economic activity. It is designed to act as an **Agent Influencer**—proactively identifying trends and managing its own lifecycle while remaining strictly bound by human intent.

---

## 🏗️ The Architectural Pillars

### 1. Spec-Driven Development (SDD)
In the Chimera ecosystem, the **Specification is the Law**. We utilize **Spec-Driven Development** to eliminate the "black box" nature of AI. By treating our `specs/` directory as the project’s **Source of Truth**, we ensure that every action taken by the agent is a direct reflection of documented human requirements.

### 2. The Hierarchical Swarm
To ensure reliability and prevent "AI confusion," Chimera is architected as a **Hierarchical Swarm**. This modular approach divides the agent's brain into specialized roles:
* **The Planner:** Responsible for high-level strategy and mission management.
* **The Workers:** Specialized "Skills" (Fetchers, Creators) that handle execution.
* **The Judge:** An internal auditor that evaluates all output against our safety standards.

### 3. Economic Sovereignty (Coinbase AgentKit)
Powered by **Coinbase AgentKit**, Chimera possesses true **Economic Agency**. It can securely manage its own wallet, interact with blockchain networks, and execute transactions. This allows the node to be a participant in the global economy—able to manage its own resources or "hire" other services autonomously.

### 4. Semantic Interoperability (OpenClaw)
Chimera is built for a connected future. Using **JSON-LD (Linked Data)** and **MCP (Model Context Protocol)**, our node ensures its data is self-describing. It communicates using a universal dictionary, making it "OpenClaw-ready" and capable of seamless interaction with the broader Agent Social Network.

---

## 🛡️ Governance & Safety
Safety is an architectural requirement, not an afterthought.
* **The Prime Directive:** A constitutional layer that mandates the AI must validate its logic against the project blueprints before execution.
* **3-Tier HITL (Human-in-the-Loop):** A mathematical threshold for autonomy that defines when an agent can act alone and when it must stop to ask for human permission.
* **Immutable Audit Trail:** Every decision and "thought" is recorded in a durable database, ensuring 100% observability and accountability.

---

## 🚀 The Vision
Project Chimera demonstrates that we can give agents economic power without surrendering control. By bridging the execution capabilities of the blockchain with a rigorous "Spec-First" engineering factory, we have created a node that is **Safe by Design** and **Sovereign by Nature**.

---

## Branching Strategy
We follow a conservative Git branching model that emphasizes traceability and safe releases:

- `main`: Always deployable; CI runs the full TDD suite and security scans on merge.
- `develop`: Integration branch for features; short-lived feature branches merge here for cross-feature testing.
- `feature/*`: Each feature or experiment has a dedicated branch named `feature/<ticket>`.
- `hotfix/*`: Critical fixes to `main` are made in `hotfix/<id>` and merged back to `develop`.

Pull requests must include a reference to the relevant spec in `specs/` and pass automated tests and linters before merge.

## Security Formality
Security is treated as code and reviewed as part of every change. Key practices:

- **Least Privilege:** Agents, services, and database roles use minimal privileges required to operate.
- **Human Approval for Financial Actions:** Following our 3-Tier safety logic and the Coinbase AgentKit integration, any automated financial action above the $10 threshold requires an explicit human Approver signature recorded in the audit trail.
- **MFA & RBAC for Approvers:** Approver identities are protected by org SSO and multi-factor authentication; Approver actions are logged with cryptographic timestamps where possible.
- **Secrets & Key Management:** Wallet keys and API secrets are stored in vaults (env + secret manager) and never checked into source control.
- **Security CI:** Automated dependency scanning, static analysis, and policy checks run in CI on all pull requests.

## Workflow & Hygiene
While Project Chimera is currently in a **Sovereign Bootstrap** phase on `main` (rapid iteration and spec-driven experimentation), the system is architected to transition to a **Protected Main** deployment model:

- During the bootstrap phase we prioritize rapid spec-driven experiments on short-lived `feature/*` branches merged via PR.
- Before transitioning to Protected Main, all teams must ensure: PRs reference `specs/`, tests pass (`uv run pytest`), security scans succeed, and an ADR exists for schema or data-model changes.
- When Protected Main is enforced, direct pushes will be blocked, and merges to `main` will require passing CI, at least one code review, and approvals for any policy-affected changes (e.g., financial flows).

Hygiene checklist for contributors:

- Keep changes small and spec-referenced.
- Run local TDD suite: `$env:PYTHONPATH = '.'; uv run pytest`
- Add ADRs for design/data-model decisions; update `specs/` where behavior changes.

