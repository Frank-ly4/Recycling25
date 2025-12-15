# Prompt — Participation-Tier Financial Analysis

Model: gpt-5-high (for structured calc + narrative), then claude-4-opus (stress-test), optional o4-mini (sanity check tables).

Context files:
- docs/GoToMarket/Pricing_Analysis_0907.md
- docs/BusinessPlan/00_Business_Plan.md

Tasks:
1) Define assumptions table (units/building, buildings/cluster, costs, price bands, participation tiers).
2) Compute revenue under building-paid vs active-paid for 25/50/75/100% tiers; include package/block upgrades.
3) Calculate break-even building counts at 25% tier for Bangkok baseline; include access-tier surcharges and fuel/materials adjustments.
4) Sensitivity: competitor undercut −30%, diesel +20%, facility +15%, labor +10%.
5) Output: concise tables + decision notes; update `Pricing_Analysis_0907.md` sections.

Deliverables:
- Tables for revenues, costs, margins by tier and by access tier.
- Break-even buildings needed at 25% tier, with clear assumptions.
- Recommendations for pricing floors and required minimums.

Handshake:
- PHASE COMPLETE – Switch to claude-4-opus for scenario stress-tests.
