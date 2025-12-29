# Bangkok Condo Dataset — Intake Checklist (for TAM)

**Goal:** Replace extrapolations with a defensible dataset for TAM/SAM/SOM.

## Minimum required fields
- Building name (or unique ID)
- Location (khet or district)
- Unit count (or range)
- Building type (condo / apartment / mixed-use) if available
- Last updated date + publisher/source

## Acceptable sources
- REIC datasets/reports (preferred)
- BMA / district registries (if accessible)
- Other credible Thai real estate datasets with provenance

## File formats
- CSV/Excel (preferred), or PDF (acceptable if tabular)

## Where to store
- `business_plan_rebuild/evidence/market/` for PDFs/exports
- If CSV/Excel is sensitive: store redacted excerpt in repo + keep originals off-repo, and document in `evidence_register.json` with a redacted pointer.

## What to update after acquisition
- `appendices/research_briefs/market/20251215_TAM_Sizing_Methodology.md` (math + dataset link)
- `market_analysis.md` TAM figures
- `INVESTOR_QA_151225.md` questions `MO-01` / `MO-03`

