## Model Handoffs (Operational Prompts)

### Phase A — o4-mini (quick calls + confirmations)
- Goal: Populate named contacts and confirm fee tables and permit checklists.
- Prompt: “Call district offices (Watthana, Khlong Toei, Sathorn, Phaya Thai) to obtain written waste fee tables and ‘detrimental to health’ permit checklists; fill `verified_contacts.md` with names/roles; attach PDFs/links.”
- Exit criteria: `verified_contacts.md` has named officers + file links; discovery file updated.
- Handshake: PHASE COMPLETE – Switch to gpt-5-high

### Phase B — gpt-5-high (docs drafting)
- Goal: Produce SLA/KPI one‑pager and pricing guardrails including package/blocks and surcharges; update pilot agreement clauses.
- Prompt: “Draft `SLA_KPI_OnePager.md` and `Pricing_Guardrails.md` reflecting access tiers, package/blocks, fuel surcharge, materials floors; integrate clauses into pilot agreement template.”
- Exit criteria: docs saved and referenced; pricing analysis updated.
- Handshake: PHASE COMPLETE – Switch to claude-4-opus

### Phase C — claude-4-opus (stress tests + scenarios)
- Goal: Sensitivity analysis and scenario stress test (undercut, low participation, access delays).
- Prompt: “Build a sensitivity grid and 3 scenarios; validate margins vs. costs; recommend go/no‑go heuristics per access tier.”
- Exit criteria: sensitivity table and scenario writeups added; go/no‑go confirmed.
- Handshake: PHASE COMPLETE – Switch to claude-4-sonnet

### Phase D — claude-4-sonnet (contract integration + outreach scripts)
- Goal: Translate guardrails into contract clauses and sales scripts (TH/EN).
- Prompt: “Embed pricing guardrails and upgrade rules in pilot agreement; generate bilingual outreach scripts and LOI.”
- Exit criteria: templates finalized and stored; sales kit updated.
