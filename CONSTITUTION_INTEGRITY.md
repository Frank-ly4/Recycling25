# Constitution — Integrity, Agents, and Flow

## Purpose
Ensure evidence-backed outputs, eliminate placeholders in outward-facing docs, and run agents in a predictable order with integrity checks and logging.

## Integrity Principles
- Evidence-first: Any number (THB, %, units, km, kgCO2e, dates) must cite a source, calc, or dataset.
- No placeholders (customer/investor-facing): reject "[TO BE]", "[PENDING]", "[TBD]", "[XX]", "[X,XXX]", "[N]".
- Confidence + review dates: tag major estimates with confidence (0.0–1.0) and next-review date.
- Version critical factors: CO2e factors and financial drivers are versioned, dated, and cited.
- Repo of record: store proofs under `research/evidence/**/*` and link from the artifact section that uses them.

## Agent Runbook (ordered)
1) QA probe (baseline)
   - Goal: inventory, coverage, placeholder/citation scan, financial sanity.
   - Review: `.cursor/qa/*` outputs; append log entry in `.cursor/qa/INTEGRITY_CHECK_LOG.md`.

2) Strategy analyst
   - Produce/refresh `docs/BusinessPlan/strategy_summary.md`, `market_segmentation.md` (Bangkok-specific with citations).
   - Block: FAIL if estimates lack citations or confidence < 0.6.

3) Finance modeler
   - Produce/refresh `finance/financial_model.csv`, `pricing_catalog.csv`, `assumptions.md`.
   - Must: >=10% margins, >=50,000 THB monthly profit within 36 months, cited costs.

4) Operations planner
   - Produce/refresh `ops/facility_plan.md`, `hiring_plan.md`, `ops_risk_matrix.md`.
   - Must: Bangkok salary/rent/vendor citations; note assumptions to verify.

5) Compliance reviewer
   - Produce/refresh `legal/legal_gap_list.md`, flag placeholders, list permits/timelines with citations.

6) QA probe (post)
   - Re-run probes; coverage >=80% on artifact types; no placeholders in outward-facing docs.

7) Marketing/research (as needed)
   - Marketing plan and research bibliography; re-run QA.

## Integrity Checks (every gate)
- Placeholder scan: none allowed in outward-facing docs.
- Citation check: numeric claims must reference a URL, doc, or calc.
- CO2e/financial factor version check: version/date present.
- Log: append an entry to `.cursor/qa/INTEGRITY_CHECK_LOG.md`.

## Evidence Management
- Save quotes/permits/regs/screenshots in `research/evidence/{category}/YYYYMMDD_*`.
- Link evidence in artifacts and in the Integrity Log entry.

## Promotion Gates
- internal_review: zero blockers; placeholders allowed only in internal templates; citations present for all public metrics.
- investor_ready: zero placeholders anywhere referenced; all numeric claims cited; QA probe PASS.

## Roles
- Owner/Approver: Frank-ly4
- QA lead: qa_probe_agent operator (or delegate)
- Evidence steward: research lead (links and storage hygiene)


