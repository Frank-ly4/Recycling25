# Web Research Log (Market Benchmarks) — 2025-12-15

## Purpose
Benchmark sources used to answer investor due diligence questions where internal data is incomplete.

## Searches performed
- **Query**: `Thailand plastic bottle recycling rate Bangkok residential sector PET collection rate national average Pollution Control Department`
  - **Outcome**: Identified benchmark sources; PCD PDF was blocked by WAF when fetched directly.

- **Query**: `Mapping Local Plastic Recycling Supply Chains Insights from Selected Cities in Thailand PDF`
  - **Outcome**: Downloaded Circulate Initiative report (Bangkok city recycling benchmark).

- **Query**: `Thailand generates approximately 2 million metric tons of plastic waste only a quarter recycled`
  - **Outcome**: Downloaded US-ASEAN Plastics Biannual Report (Thailand national plastic waste benchmark).

## Downloaded evidence (stored locally)
- `business_plan_rebuild/evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`
  - Notes: Contains Bangkok benchmark statement (e.g., ~15% or 134 kt/year plastic waste recycled; informal sector role). Extracted via local PDF text parsing.

- `business_plan_rebuild/evidence/market/20251215_iucn_thailand_plastic_hotspotting_guidance.pdf`
  - Notes: Contains Thailand plastic flow/recycling table data (needs careful interpretation with page headers).

- `business_plan_rebuild/evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
  - Notes: Contains Thailand national plastic waste generation/recycling benchmark statement.

## Access issues
- **PCD (Pollution Control Department) PDF** from `pcd.go.th` was blocked by Incapsula/WAF from this environment at the time of retrieval (not archived).
