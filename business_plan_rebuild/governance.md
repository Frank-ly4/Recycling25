# Governance and Approval Protocol

## 1. Purpose
To ensure all artifacts in the `business_plan_rebuild` directory meet investor-ready standards, are evidence-backed, and have been reviewed before finalization.

## 2. Roles and Responsibilities
- **Business Owner**: Final strategy approval and investor alignment.
- **Finance Lead**: Validation of assumptions, P&L, and repayment logic.
- **Ops Lead**: Feasibility check of logistics, routes, and labor.
- **Compliance/Audit**: Verification of regulatory alignment (BMA, DLT) and artifact integrity.

## 3. Approval Gates
Each artifact must pass the following gates before being marked "FINAL":

### Gate 1: Structure & Completeness
- [ ] File exists in correct directory.
- [ ] Follows standard markdown/JSON structure (or appropriate data format).
- [ ] All sections defined in the plan are present.

### Gate 2: Evidence Check
- [ ] Key claims have citations (e.g., "Source: REIC 2024", "Source: Supplier Quote").
- [ ] Assumptions are explicitly flagged (e.g., "ASSUMPTION—VALIDATE").
- [ ] All material claims are tracked in `evidence_register.json` with status (verified vs assumption) and validation method.
- [ ] Financial figures align with `financials/assumptions.json`.

### Gate 3: Investor Readiness
- [ ] Tone is professional, concise, and persuasive.
- [ ] Risks are acknowledged and mitigated.
- [ ] Formatting is clean (headers, tables, lists).

## 4. Change Management
- All changes to finalized documents must be logged in `audit_trail.jsonl`.
- Significant strategic pivots (e.g., pricing model change) require full team consensus.

## 5. Acceptance Tests
- **Financial Viability**: Model shows ≥60k THB/month profit by Month 18.
- **Regulatory Compliance**: Legal doc cites specific BMA/DLT regulations.
- **Operational Reality**: Ops plan accounts for Bangkok traffic, waste density, and labor laws.

