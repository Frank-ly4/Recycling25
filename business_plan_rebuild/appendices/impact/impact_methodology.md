# Impact Methodology (CO₂e Diversion)

**Status:** Draft (desk-ready; to be localized)  
**Last updated:** 2026-01-02  
**Owner:** Operations / Impact

## 1) Scope
This methodology defines how Recycling25 estimates **CO₂e avoided** from recyclable materials collected and diverted to recycling.

### Included
- Building-level material weights (kg) by stream (e.g., PET, HDPE, aluminum, paper).
- A single CO₂e factor per material stream.

### Excluded (tracked separately if/when measured)
- Collection vehicle fuel/emissions
- Facility electricity/emissions
- End-processor energy mix and yield losses (unless explicitly modeled)

## 2) Calculation logic

### Inputs (per reporting period)
- \(m_{i}\): mass collected for material \(i\) (kg)
- \(f_{i}\): CO₂e factor for material \(i\) (kgCO₂e per kg material)

### Output
\[
CO2e\_avoided = \sum_{i} m_{i} \times f_{i}
\]

## 3) Units and definitions
- **Mass**: kilograms (kg)
- **CO₂e avoided**: kilograms of CO₂-equivalent (kgCO₂e)
- **Factor meaning**: proxy “avoided emissions” for recycling vs baseline virgin production/disposal pathway as defined by the factor source.

## 4) Data sources and auditability

### 4.1 Weight data (primary)
- Scale tickets / weight logs (preferred)
- Processor weighbridge receipts (preferred for offtake validation)

### 4.2 Weight data (secondary)
- Pickup photos (no faces) + bin counts (only if scale unavailable; must be labeled estimate)

### 4.3 Reporting format
- Monthly report format: `outreach_kit/diversion_report_template.md`

## 5) CO₂e factors (current proxy set)
- Factors are maintained in the evidence memo: `evidence/impact/20260102_co2e_factors.md`

## 6) Validation approach (to move beyond desk-ready)
- During pilots, reconcile building-scale logs to processor receipts monthly.
- If/when Thailand/ASEAN-specific LCA factors are sourced, replace proxy factors with localized factors and record version/date.


