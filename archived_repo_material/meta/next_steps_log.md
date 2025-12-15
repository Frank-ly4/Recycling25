# Next Steps Log — Bangkok Condo Recycling

Date: 2025-09-07
Status: Ready for Phases A–D execution

## Current State Summary
- **Pricing analysis complete**: 50% tier @90 THB with 5 buildings is optimal for Bangkok launch
- **Stress testing complete**: Documented methodology and go/no-go heuristics by access tier
- **Service tiers defined**: 25%/50%/75%/100% with realistic pricing and building requirements
- **Templates ready**: RFI templates for BMA, DIW, RD, BOI, processors, brokers, DLT, Isuzu, PDPC
- **Contacts scaffold ready**: `research/evidence/contacts/verified_contacts.md` for named officers

## Phases A–D Ready for Execution

### Phase A — o4-mini (Quick confirmations and contacts)
**Goal**: Populate named contacts and confirm fee tables/permit checklists
**Tasks**:
- Call BMA district offices (Watthana, Khlong Toei, Sathorn, Phaya Thai) using `research/evidence/templates/BMA_RFI.md`
- Fill `research/evidence/contacts/verified_contacts.md` with names/roles
- Attach PDFs/links for waste fee schedules and permit requirements
**Exit criteria**: Named officers + file links; discovery file updated
**Handshake**: PHASE COMPLETE – Switch to gpt-5-high

### Phase B — gpt-5-high (SLA/KPI docs + pricing guardrails)
**Goal**: Draft SLA/KPI one-pager and pricing guardrails with package/blocks and surcharges
**Tasks**:
- Create `SLA_KPI_OnePager.md` with specific metrics (miss rate, response time, credits)
- Create `Pricing_Guardrails.md` reflecting access tiers, package/blocks, fuel surcharge, materials floors
- Integrate clauses into pilot agreement template
**Exit criteria**: Docs saved and referenced; pricing analysis updated
**Handshake**: PHASE COMPLETE – Switch to claude-4-opus

### Phase C — claude-4-opus (Sensitivity and scenarios — ALREADY COMPLETED)
**Goal**: Stress-test scenarios and sensitivity grid ✓ DONE
**Output**: `docs/GoToMarket/Pricing_Stress_Test_0907.md`
**Handshake**: PHASE COMPLETE – Switch to claude-4-sonnet

### Phase D — claude-4-sonnet (Contract integration + outreach scripts)
**Goal**: Translate guardrails into contract clauses and sales scripts (TH/EN)
**Tasks**:
- Embed pricing guardrails and upgrade rules in pilot agreement
- Generate bilingual outreach scripts and LOI templates
- Update sales kit with finalized templates
**Exit criteria**: Templates finalized and stored; sales kit updated

## Key Files to Reference
- `070925assessment` — Canonical business plan audit (Sections 1–9)
- `070925_action_plan.md` — Dependency-based task flow
- `docs/GoToMarket/Pricing_Stress_Test_0907.md` — Stress testing methodology and results
- `docs/GoToMarket/Pricing_Tiers_Results_0907.md` — Service tier pricing and building requirements
- `discovery_responses3.md` — Fact-checks, RFIs, and evidence gaps
- `research/evidence/templates/` — Send-ready RFI templates
- `CONSTITUTION.md` — Process rules (change-log-first, dependency graph, persistence)

## Critical Business Decisions Made
1. **Target**: 50% service tier @90 THB/unit with 5 buildings minimum
2. **Pricing floors**: A=80, B=90, C=100 THB by access tier
3. **Service model**: 100% of units billed; tier determines included volume/engagement
4. **Materials revenue**: Bonus only via MOUs; not included in base viability
5. **Fuel hedge**: Surcharge trigger if diesel >38 THB/L for 30 days
6. **Package/blocks**: 100-unit blocks with micro-cluster minimum (≥300 units across ≥2 buildings)

## Copy-Paste Prompts for Fresh Chat

**Phase A Prompt (o4-mini)**:
```
You are o4-mini. Read: research/evidence/templates/BMA_RFI.md, research/evidence/contacts/verified_contacts.md, discovery_responses3.md. Task: Call BMA district offices (Watthana, Khlong Toei, Sathorn, Phaya Thai) to obtain written waste fee tables and permit checklists; fill verified_contacts.md with names/roles; attach PDFs/links. Exit: Named officers + file links ready. Handshake: PHASE COMPLETE – Switch to gpt-5-high
```

**Phase B Prompt (gpt-5-high)**:
```
You are gpt-5-high. Read: docs/GoToMarket/Pricing_Stress_Test_0907.md, docs/GoToMarket/Pricing_Tiers_Results_0907.md, docs/BusinessPlan/00_Business_Plan.md. Task: Draft SLA_KPI_OnePager.md and Pricing_Guardrails.md reflecting access tiers (A/B/C), service tiers (25/50/75/100%), package/blocks, fuel surcharge, materials floors; integrate clauses into pilot agreement template. Exit: Docs saved and referenced. Handshake: PHASE COMPLETE – Switch to claude-4-opus
```

**Phase D Prompt (claude-4-sonnet)**:
```
You are claude-4-sonnet. Read: SLA_KPI_OnePager.md, Pricing_Guardrails.md, research/evidence/templates/. Task: Embed pricing guardrails and upgrade rules in pilot agreement; generate bilingual (TH/EN) outreach scripts and LOI templates; update sales kit. Exit: Templates finalized and stored; sales kit updated.
```

## Immediate Next Actions When Resuming
1. Start with Phase A (o4-mini) — populate contacts and get official fee schedules
2. Skip Phase C (already completed stress testing)
3. Execute Phases B and D in sequence
4. Update `discovery_responses3.md` with confirmed findings
5. Generate lightweight templates for actual pilot use

## Context for Fresh Chat
This is a Bangkok condo recycling service business plan. We've completed financial modeling showing 50% service tier @90 THB/unit with 5 buildings is optimal. We have RFI templates ready and need to execute contact verification and document creation phases. All files are saved and persistent per `CONSTITUTION.md` rules.
