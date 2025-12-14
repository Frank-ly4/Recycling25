# Coverage Matrix — Business Plan Components (Bangkok)

Generated: 2025-11-01

| Artifact Type            | Covered | Evidence(s)                                                         | Issues / Notes |
|--------------------------|---------|----------------------------------------------------------------------|----------------|
| strategy_doc             | Yes     | docs/BusinessPlan/00_Business_Plan.md                                | Ensure all numeric claims have citations and confidence tags |
| financial_model          | Yes     | finance/financial_model.csv                                          | Run probes for ≥10% margins and ≥50k THB/mo ≤36 months; sanity on growth |
| pricing_catalog          | Yes     | finance/pricing_catalog.csv                                          | Header matches required fields; confirm margins and package descriptions |
| go_to_market_plan        | Yes     | docs/GoToMarket/01_Validation_Sprint.md; 03_OnePager.md; 04_Deck...  | Ensure building-level billing narrative aligned with packages |
| operations_manual        | Yes     | ops/SOPs/*; ops/facility_plan.md; ops/hiring_plan.md                 | Verify citations for facility quotes, wages, fuel, vehicle/insurance |
| contracts                | Yes     | docs/GoToMarket/06_Service_Agreement_12m.md; preservation/**         | Confirm placeholders removed; SLA metrics aligned to SOP |
| research_bibliography    | Yes     | research/evidence/**/*                                               | Ensure each claim in plan links to a specific evidence file |
| audit_log                | Yes     | .cursor/qa/INTEGRITY_CHECK_LOG.md                                    | Append entries at each gate |

## Immediate Follow-ups
- Re-run financial probes per `.cursor/specify.json` rules (margins, profit target, sanity thresholds).
- Placeholder/citation scan for outward-facing docs (Business Plan core and Go-To-Market set).
- Align Risks & Mitigations with SWOT and Five Forces mitigations from `discovery_responses5.md`.

## Scan Results (snapshot)
- Placeholder tokens found in `preservation/necessary_documentation/36_Crisis_Communication_Plan.md` rows 477–482; treated as internal template (not outward-facing). Customize prior to publication.
- Preliminary financial sanity: pricing margins ≥10% and model reaches ≥50k THB/mo by Month 4–5 in current CSV; confirm via automated probe.