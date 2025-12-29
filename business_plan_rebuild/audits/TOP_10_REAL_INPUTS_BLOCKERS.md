# Top 10 Real-Inputs Blockers (Execution + Pitchworthiness)

**Source of truth:** `audits/DD_GAP_REGISTER_151225.md`  
**Evidence workflow:** `EVIDENCE_WORKFLOW.md`

## 1) Official cap table (shareholder register)
- **Why it blocks:** No investor will proceed without clean ownership.
- **Close criteria:** Fill `cap_table.md` from the official shareholder register; list options/convertibles or explicitly state NONE.
- **Gap IDs:** `CC-01`…`CC-04`

## 2) Named team bios + conflicts statement
- **Why it blocks:** Execution-heavy business; roles must be real.
- **Close criteria:** Replace TBDs in `team_bios.md` and add signed conflicts/related-party statement (or “NONE”).
- **Gap IDs:** `TF-01`…`TF-10`

## 3) Insurance quotes / bound policy schedules (redacted)
- **Why it blocks:** Logistics + waste = incident risk; investor expects coverage.
- **Close criteria:** Archive broker quote(s)/policy schedules in `evidence/insurance/` and update `insurance_program.md`.
- **Gap IDs:** `IC-01`, supports `OR-04`

## 4) DLT classification closure (or license-bridge contract)
- **Why it blocks:** Transport classification is a stoppage risk.
- **Close criteria:** Written DLT confirmation for “recyclables pickup + service fee” OR executed licensed-operator bridge contract + inspection packet.
- **Gap IDs:** supports `CLAIM-DLT-YELLOW-001`

## 5) BMA permit process specifics for the chosen district
- **Why it blocks:** You need an actionable filing path for commercial operation.
- **Close criteria:** Archive district guidance/forms or a field memo with office, contact, steps, and receipts.
- **Gap IDs:** supports `legal_compliance.md`

## 6) Pilot customer commitments (LOI / Pilot SLA)
- **Why it blocks:** Without signed pilots, the business is still theoretical.
- **Close criteria:** 1–3 redacted signed pilot SLAs/LOIs archived under `evidence/contracts/`.
- **Gap IDs:** supports `MO-10`, enables `BM-07`

## 7) Fleet + facility quotes (lease + warehouse + equipment)
- **Why it blocks:** The model depends on real Bangkok quotes.
- **Close criteria:** Redacted quotes/contracts archived (fleet lease/operator, warehouse lease/deposit, scale/baler).
- **Gap IDs:** `CLAIM-LEASE-001`, `CLAIM-RENT-001`, `CLAIM-LEASE-PARTNER-001`, `TP-09`

## 8) Bangkok TAM dataset (replace extrapolation)
- **Why it blocks:** “TAM hand-waving” is a fast investor kill.
- **Close criteria:** Archive a defensible dataset (REIC/BMA/credible equivalent) and rebuild the sizing table with transparent math.
- **Gap IDs:** `MO-01`, `MO-03`, `CLAIM-REIC-SIZE-001`

## 9) CAC + funnel metrics plan (and first measurements)
- **Why it blocks:** Investors will ask “how do you acquire condos and at what cost?”
- **Close criteria:** Funnel tracking + CAC range after first 10–20 deal cycles.
- **Gap IDs:** `BM-07`

## 10) Offtake buyer terms / specs
- **Why it blocks:** Material has to exit your system on known terms.
- **Close criteria:** Processor MOU/terms/specs and payment terms (even if pilot-only) archived.
- **Gap IDs:** supports offtake questions; closes parts of `operations_plan.md` assumptions.

