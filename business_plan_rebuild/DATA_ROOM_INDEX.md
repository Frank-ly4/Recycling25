# Data Room Index (Investor)

## 1. Recommended Reading Order (30–45 minutes)
- **Start here**: `README.md`
- **One-page narrative**: `executive_summary.md`
- **Market + why now**: `market_analysis.md`
- **How we execute**: `operations_plan.md`
- **Financial engine**:
  - `financials/model_inputs.json` (single source of truth for all drivers)
  - `financials/model_spec.md` (formulas + accounting/cash policy)
  - `financials/projections.json` (generated monthly P&L-like view)
  - `financials/cashflow.json` (generated cash movement + balances)
  - `financials/waterfall.json` (generated investor repayment schedule)
  - `financials/sensitivity_analysis.md` (stress tests; must match the generated model)
  - `investor_relations.md` (deal terms + narrative explanation of `waterfall.json`)
  - _(compatibility)_ `financials/assumptions.json` (deprecated pointer to `model_inputs.json`)
- **Regulatory + contractual**:
  - `legal_compliance.md`
  - `outreach_kit/contract_template.md` (Updated with Thailand VAT/Liability)
  - `outreach_kit/SLA_checklist.md`
- **Risk & controls**:
  - `risk_register.md`
  - `governance.md`
  - `audit_trail.jsonl`

## 2. Evidence & Diligence Trail
- **Evidence folder**: `evidence/` (source PDFs, screenshots, quotes)
- **Audit memos** (internal): `audits/`
  - `audits/INVESTOR_QA_CHECKLIST.md` **(Start Here for Due Diligence Defense)**
  - `audits/pilot_validation.md` (90-Day Commercial Proof Plan)
  - `audits/red_team_gap_analysis.md`
  - `audits/vehicle_specs_comparison.md`
  - `audits/viability_check.md`

## 3. What’s “Investor Grade” in this Pack
- Every key claim is either:
  - **Sourced** (link + excerpt), or
  - **ASSUMPTION—VALIDATE** (range + validation plan).
- Financials reconcile across:
  - **Inputs → P&L → Cashflow → Investor Waterfall**.
- Commercial reality check:
  - Contract updated for VAT (7%) and WHT (3%).
  - Ops plan aligned with BMA regulations and Truck Ban windows.

## 4. Open Diligence Items (Tracked)
These items are tracked in `evidence_register.json` and will be closed during the pilot validation sprint.
