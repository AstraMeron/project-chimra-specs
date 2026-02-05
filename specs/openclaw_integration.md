OpenClaw Integration

Plan: Broadcast agent availability for skill-based microservices.

1. Agent Registration: On startup, each skill agent will POST an availability message
   to the OpenClaw broker with metadata: skill_name, version, capabilities, endpoint.

2. Heartbeat: Agents send a periodic heartbeat every 30s to the broker to indicate liveness.

3. Discovery API: The broker exposes a /agents endpoint listing active agents and their
   capabilities; orchestrators query this to route requests.

4. Security: All agent-broker communication uses TLS and mutual auth; tokens rotate
   and are validated against a central auth service.

5. Monitoring: Broker emits metrics (uptime, latency, errors) to central observability.

6. Governance Hook: The broker validates AI review via `.coderabbit.yaml` rules before
   advertising a new agent as available.
