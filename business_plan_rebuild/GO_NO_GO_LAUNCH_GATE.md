# Go/No-Go Launch Gate (Execution Readiness)

**Purpose:** One-page checklist of the *real-world inputs* required before we can execute operations safely and credibly.

**Source of truth for what’s still open:** `audits/DD_GAP_REGISTER_151225.md`  
**Evidence rules:** `EVIDENCE_WORKFLOW.md`

## How to use
- Mark each gate **GO** only when the “Close criteria” is met and the evidence is archived under `evidence/`.
- If any gate is **NO-GO**, we do not launch beyond a contained pilot.

## Gate A — Corporate + ownership hygiene (Investor/Legal blocker)
- [ ] **GO**: Official shareholder register reconciled into `cap_table.md` (and any instruments explicitly listed as **NONE** or detailed).
- [ ] **GO**: Equity option artifacts are internally consistent (even if equity is optional): `equity_terms_summary.md` + `dilution_model.md`.

**Closes:** `CC-01`..`CC-04` (and enables `CC-02`, `CC-03`)  
**Owner:** Finance / Governance  
**Evidence required:** shareholder register PDF (archive in `evidence/legal_corporate/`)

## Gate B — Team and governance is real (Execution blocker)
- [ ] **GO**: Named founders and key operators listed in `team_bios.md` (no TBDs), with responsibilities and conflict disclosure.
- [ ] **GO**: Governance cadence and approvals are agreed (see `governance.md`).

**Closes:** `TF-01`..`TF-10` (as bios are filled)  
**Owner:** Founder / Governance  
**Evidence required:** CVs/links (optional) archived in `evidence/team/`

## Gate C — Regulatory posture (Thailand-specific, launch-killer)
- [ ] **GO**: BMA “Business Detrimental to Health” permit path is actionable for the chosen district (forms/process evidence archived).
- [ ] **GO**: DLT classification risk closed (written confirmation archived) OR license-bridge operator contract executed and inspection packet ready.

**Closes:** `CLAIM-DLT-YELLOW-001` (and any BMA process gaps), supports `legal_compliance.md`  
**Owner:** Legal/Compliance  
**Evidence required:** regulator email/letter, district office guidance, executed operator/lease docs (archive in `evidence/bma/`, `evidence/dlt/`, `evidence/legal_corporate/`)

## Gate D — Insurance bound (Operational/Investor blocker)
- [ ] **GO**: Broker quote(s) or bound policy schedule(s) archived; coverage stack aligns to `risk_register.md`.
- [ ] **GO**: Incident/claims process owner named and SOP in place (reference `operations_plan.md` H&S/crisis section).

**Closes:** `IC-01`, supports `OR-04`  
**Owner:** Ops  
**Evidence required:** broker quote/policy schedule (archive in `evidence/insurance/`)

## Gate E — Fleet + facility + equipment ready (Physical execution)
- [ ] **GO**: Primary vehicle + rescue strategy available (owned/leased) with maintenance/replacement plan.
- [ ] **GO**: Facility secured (lease/deposit) and planned machinery remains under thresholds (Factory Act plan).
- [ ] **GO**: Weighing + logging + baling plan is executable (scale/baler access or staged plan).

**Supports:** pilot execution + unit economics validation (`MO-02`, `OR-04`)  
**Owner:** Ops  
**Evidence required:** executed lease(s), vendor quote(s), equipment specs (archive in `evidence/facility/`, `evidence/vendors/`)

## Gate F — Commercial readiness (cash collection and contracts)
- [ ] **GO**: Canonical contract terms are enforceable in reality (deposit + Net-15/advance billing + suspension for arrears).
- [ ] **GO**: At least one pilot/customer commitment is signed (pilot SLA or LOI) and onboarding kit is ready.

**Closes/Supports:** `BM-07` (CAC data collection begins), `MO-10` (pipeline tie-in)  
**Owner:** Sales  
**Evidence required:** signed pilot SLA/LOI (archive in `evidence/contracts/`)

## Gate G — Measurement + reporting works end-to-end (your product)
- [ ] **GO**: Pilot KPI schema captures **kg/building/month** and **PET kg/building/month** (see `appendices/pilots/bangkok-zone-a/kpis.md`) and is actually being recorded.
- [ ] **GO**: Monthly ESG/diversion report template is ready and reproducible; CO2e factors documented.

**Closes:** `MO-02` (once data exists), supports `MO-04`, `EI-03`  
**Owner:** Ops / Materials / Finance  
**Evidence required:** sample logs + sample report (archive in `appendices/pilots/` and/or `evidence/`)

## Gate H — Market sizing and CAC evidence (scale readiness; not required for day-1 pilot)
- [ ] **GO**: Bangkok TAM worksheet upgraded from assumption to evidenced methodology (data sources archived).
- [ ] **GO**: CAC/funnel metrics collected from first 10–20 deals.

**Closes:** `MO-01`, `MO-03`, `BM-07`  
**Owner:** Founder / Sales  
**Evidence required:** dataset exports + research log (archive in `evidence/market/`)

## Final sign-off
- **Business Owner:** ____________  Date: ________
- **Finance Lead:** ____________    Date: ________
- **Ops Lead:** ____________        Date: ________
- **Compliance/Audit:** ____________ Date: ________

