# Bangkok Condo TAM/SAM/SOM — Sizing Methodology (Draft)

## Purpose
Upgrade MO-01/MO-03 from narrative anchors to a defensible, repeatable sizing method.

## Current state (what we have)
- Zone A SOM table exists in `market_analysis.md` but is flagged `ASSUMPTION—VALIDATE` (`CLAIM-REIC-SIZE-001`).
- Pitch deck includes a headline estimate (e.g., “1,500+ condos >300 units”).

## Investor-grade target
- A sizing workbook (even if simple) with:
  - clear segmentation (district cluster; building size tiers; condo vs apartment where feasible)
  - explicit data sources
  - reproducible math
  - sensitivity ranges

## Data sources (preferred order)
1. **REIC** condo stock tables (ideal): condo unit stock by district / submarket.
2. **BMA / district offices**: registries or public dashboards (if available).
3. **Commercial property datasets** (DDproperty / PropertyGuru / CBRE/JLL summaries) as secondary benchmarks.
4. **Internal pipeline mapping**: count of target buildings from manual mapping + site surveys.

## Method (repeatable)
1. **Define the ICP**
   - Default: 300–600 units/condo (route density + economics) and Zone A districts.
2. **Count buildings in segment**
   - Method A: REIC district tables.
   - Method B: Manual mapping: export building list, de-duplicate, tag by unit size tier.
3. **Convert to units**
   - If unit counts are available: sum units directly.
   - If only building counts: multiply by tier-average units (use low/base/high).
4. **Convert to service-fee TAM**
   - Monthly revenue = units × fee per unit per month.
5. **Convert TAM → SAM → SOM**
   - SAM = reachable districts (logistics radius + truck ban feasibility).
   - SOM = year-1 reachable buildings given sales capacity and ramp plan.

## Validation plan (to close `CLAIM-REIC-SIZE-001`)
- Acquire and archive a primary dataset (REIC or BMA equivalent) under `business_plan_rebuild/evidence/market/`.
- Rebuild the Zone A table with transparent math.
- Update `evidence_register.json` with source_url + local_path + excerpt.

## Deliverable
- Once the source data is available, we will produce:
  - Updated `market_analysis.md` sizing table (VERIFIED), and
  - An exportable building list (CSV) used for calculation (stored in `appendices/research_briefs/market/`).
