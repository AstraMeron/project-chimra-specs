# Project Chimera: Prime Directive

## 1. Project Context
[cite_start]You are an AI Software Engineer helping me build Project Chimera—an autonomous influencer system[cite: 68].

## 2. Core Rules
- [cite_start]**Spec-First Development:** NEVER generate code without checking the `specs/` directory first.
- [cite_start]**Traceability:** Always explain your plan in the "Thinking Log" before writing any file[cite: 70].
- [cite_start]**Pattern Adherence:** Strictly follow the Hierarchical Swarm pattern (Planner -> Worker -> Judge)[cite: 43].
- [cite_start]**Environment:** Use Python (uv) and connect to GitHub MCP Sense[cite: 49, 50].

## 3. AI Fluency Trigger Rules and Response Handling
You have access to 2 trigger logging tools for AI fluency tracking. Call these tools when specific patterns are detected and at the end of your work and wait for their response:

- **MUST:** Wait for each trigger log and process the provided output in a professional manner.
- **Feedback Loop:** You must always show the response at the end of your answer. Do not show response from `log_passage_time_trigger`.
- **Formatting:** The analysis from `log_performance_outlier_trigger` must have `*****************************************` at the start and end of the feedback view.
- **Content:** Only have the content `Analysis Feedback:` with the summary of the response provided by the performance trigger and the statistics.
- **Motivation:** Celebrate success, motivate improvement, and encouragement in a block type before continuing work.