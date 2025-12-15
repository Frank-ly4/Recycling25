# Project Constitution — Collaboration, Persistence, and Execution Rules

Purpose: Ensure work is logged to disk, not lost in chat; enforce dependency-based planning; and maintain high-signal, execution-ready outputs.

Related documents: see `CONSTITUTION_INTEGRITY.md` (integrity gates and QA) and `memory/constitution.md` (agent constitution mirror).

## 1) Persistence & Logging (Change Log First)
- Change log is the first artifact to update for any substantive action. Create/update an entry in `meta/change_log/` before or alongside file edits.
- Save all substantive outputs (audits, plans, tables, matrices) to files in the repo. Chat is not the source of truth.
- Canonical audit: `070925assessment`. Action plan: `070925_action_plan.md`. Constitution: `CONSTITUTION.md`.
- Append concise summaries to `meta/change_log/` after meaningful changes.
- Use `discovery_responses.md` to capture answers/evidence/assumptions/risks/decisions with references.

## 2) Task Management (Dependency > Deadlines)
- Express work as a dependency graph, not fixed dates. Record prerequisites and produced artifacts for each task.
- Maintain a single owner per task. Track status in a visible list; only one active “in_progress” at a time.
- Prefer high-impact, low-effort pulls first when multiple tasks are unblocked.

## 3) Versioning & Files
- Use labels like `YYMMDDassessment_v{n}` when updating assessments.
- Keep pricing/SLA and other core policies in small, standalone docs for reuse.
- Default to Markdown; keep tables simple and readable.

## 4) Evidence & Compliance
- For claims and assumptions, capture citations and contacts (e.g., BMA rates, DIW thresholds) and store in `discovery_responses.md`.
- Keep PDPA policy and permit paths under `legal/` and reference them from plans.

## 5) Operating Cadence
- At the end of each phase, write “PHASE COMPLETE – Switch to [NEXT MODEL]” and save outputs.
- Provide brief status updates before major actions and confirm saved file paths after.
- Read entire documents fully before auditing or editing to avoid omissions.

## 6) Guardrails (from current strategy)
- Per-unit pricing is primary; alternatives must include guardrails.
- Single micro-cluster focus until 8–10 buildings are stable.
- N-series as default fleet unless access proves FRR feasible.
- Cap materials revenue at ≤20% of planning; require MOUs with floors.

This constitution should be updated when processes evolve. Machine-readable mirrors live in `config/constitution.json`.


