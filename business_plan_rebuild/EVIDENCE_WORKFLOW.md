# Evidence Workflow (Canonical)

## Purpose
This is the single rulebook for turning the business plan into **investor-grade**: every material claim must be backed by an archived source (or clearly labeled as an assumption with a validation plan).

## The “framework” we always reference
Use these files every time you update anything investor-facing:
- `audits/DD_GAP_REGISTER_151225.md` — execution queue (what’s open, owner, close criteria)
- `evidence_register.json` — claim registry (what claims exist, status, and evidence pointers)
- `INVESTOR_QA_151225.md` — investor-facing answers (must cite sources)
- `Comprehensive Due Diligence Questions 151225.txt` — master checklist (must stay aligned)

## Rules (non-negotiable)
1. **No invented numbers.**
2. Every claim is one of:
   - `VERIFIED` (has strong evidence),
   - `BENCHMARK` (external benchmark; clearly labeled),
   - `ASSUMPTION—VALIDATE` (not yet proven; includes close plan).
3. **Archive evidence locally** and reference it from `evidence_register.json`.

## Evidence storage convention
- Store evidence under: `business_plan_rebuild/evidence/<topic>/YYYYMMDD_<source>_<slug>.<ext>`
  - Examples: `pdf`, `html`, `png`, `md` (notes/extracts), `csv` (datasets)
- If a site is blocked (WAF), record the failure and use an alternative source.

## Required metadata in `evidence_register.json`
For every material claim used in investor-facing docs:
- `claim_id`
- `claim_text`
- `files` (where the claim is asserted)
- `source_url`
- `source_type`
- `local_path`
- `excerpt` (the exact line/table we rely on)
- `confidence`
- `status`
- `validation_method`

## Web research logging (required for benchmarks)
For every external benchmark used:
- Create `business_plan_rebuild/evidence/<topic>/YYYYMMDD_SEARCH_LOG.md` containing:
  - search term(s)
  - date
  - why relevant
  - sources considered + which chosen
  - access issues (if any)

## How to close an open diligence item (definition of done)
When you close an item in `audits/DD_GAP_REGISTER_151225.md`:
1. Add/verify evidence under `evidence/<topic>/…`
2. Update `evidence_register.json` (claim status + pointers)
3. Update `INVESTOR_QA_151225.md` answer and status
4. Update the master checklist entry in `Comprehensive Due Diligence Questions 151225.txt`
5. Ensure `DATA_ROOM_INDEX.md` points to the artifact if it’s investor-facing

## Minimal acceptance checks before sharing with investors
- No contradictions across: `market_analysis.md`, `legal_compliance.md`, `investor_relations.md`, `financials/*`
- Every number in `executive_summary.md` is traceable to either:
  - a model output (`financials/*`), or
  - an evidence artifact (`evidence/*`), or
  - explicitly labeled as an assumption (with validation plan)

