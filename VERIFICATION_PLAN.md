# Verification Plan — Assumptions and Unverified Items

## Purpose
Systematically replace assumptions with verified data and citations; track status to closure.

## Process
1. Triage weekly: prioritize High→Medium→Low.
2. Collect evidence (3 sources where feasible); save under `research/evidence/...`.
3. Update artifacts with citations; remove placeholders.
4. Re-run QA; append Integrity Log entry.
5. Close item when confidence ≥0.8 and citation(s) present.

## Register (initial)
| Item | Current Claim | Location(s) | Status | Verification Method | Evidence To Collect | Owner | Due | Target Confidence |
|---|---|---|---|---|---|---|---|---|
| Price per unit (THB) | 80–110 | docs/BusinessPlan/strategy_summary.md, finance/financial_model.csv | Assumed | 10 juristic mgr interviews + 3 competitor quotes | LOIs, competitor rate cards | Ops/Sales | +10d | ≥0.8 |
| Avg units/building | 400 | docs/BusinessPlan/market_segmentation.md | Cited (REIC) | Pull REIC district tables | REIC PDFs, table extract | Research | +7d | ≥0.9 |
| Variable cost/unit | 30 THB | finance/assumptions.md | Assumed | Bottom-up BOM + times | Supplier quotes, time&motion | Ops/Finance | +14d | ≥0.8 |
| Fixed OPEX ramp | 45k→82k | finance/assumptions.md | Assumed | Rent quotes + wage data | 3 rent quotes, JobsDB, DLPW | Finance | +14d | ≥0.85 |
| Growth ramp (units) | 400→5600 | finance/financial_model.csv | Assumed | Funnel math from marketing plan | Funnel, cycle times | Strategy/Marketing | +21d | ≥0.75 |
| Churn | 0% Y1, 5% Y2 | finance/assumptions.md | Assumed | Contract renewal analysis | Renewal clauses, comps | Ops/Legal | +30d | ≥0.7 |
| CAPEX vehicle | 800k THB | finance/assumptions.md | Assumed | Dealer quotes | Isuzu/Toyota quotes | Ops | +7d | ≥0.9 |
| Facility rent | 18–22k (init) | ops/facility_plan.md | Assumed | 3 broker quotes | CBRE/JLL/Plus quotes | Ops | +7d | ≥0.85 |
| Wages (THB/mo) | Driver 18k; Loader 12k | ops/hiring_plan.md | Assumed | JobsDB + DLPW tables | Job postings, wage tables | Ops/HR | +7d | ≥0.9 |
| Fuel price + km/L | 35 THB; 4 km/L | finance/assumptions.md | Assumed | PTT diesel history + route km | PTT charts, route model | Ops | +10d | ≥0.8 |
| Processor prices | PET/HDPE/cardboard | ops docs | Unknown | 3 processor quotes | Price sheets/emails | Ops | +14d | ≥0.8 |
| CO2e factors | Illustrative | config/co2e_factors.json | Placeholder | Thai/ASEAN LCA sources | LCA reports, factor table | Research | +21d | ≥0.85 |
| Permit timelines | BMA/DLT/Facility | legal/legal_gap_list.md | Assumed | District confirmation | Emails/forms from offices | Legal/Ops | +14d | ≥0.8 |
| PDPA roles | DPO, notices | preservation/necessary_documentation/31_PDPA_Compliance_Policy.md | Placeholder | Counsel confirmation | Final policy, DPO letter | Legal | +14d | ≥0.9 |
| SLA metrics | ≥98% on-time | ops/SOPs/* | Defined | Pilot measurement | Timestamped logs/photos | Ops/QA | +30d | ≥0.8 |

## Weekly Cadence
- Mon: Triage and owner assignment
- Thu: Evidence drop and artifact updates
- Fri: QA probe + Integrity Log update

## Done Criteria (per item)
- Artifact updated, placeholders removed
- Citations present (URL/doc) and evidence saved
- Integrity Log entry appended
- QA re-run shows PASS



## Latest Audit Artifacts
- `.cursor/qa/inventory.json` — repo components inventory
- `.cursor/qa/coverage_matrix.md` — component coverage and follow-ups
- `.cursor/qa/readiness_scorecard.md` — PASS/PRE-PASS status by component
- `.cursor/qa/gap_list.md` — prioritized remediation items with effort/impact

## Open Gaps Snapshot
- All previously listed gaps have been addressed. See `.cursor/qa/gap_list.md` for completion notes and artifact paths.
