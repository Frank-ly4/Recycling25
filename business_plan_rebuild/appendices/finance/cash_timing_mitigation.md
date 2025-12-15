# Cash Timing Mitigation (Bangkok Execution)

This note documents practical, Bangkok-feasible mitigations for the cash timing trough identified in the generated base case (`financials/cashflow.json`, Month 15 cash_end = -23,040 THB).

## 1) Contract terms (primary lever)
Use **advance billing + Net-15** and **automatic service suspension** for >30 days overdue, per the canonical template:
- `outreach_kit/service_agreement_12m.md`

Add (Schedule A) as standard:
- Security/equipment deposit (bins/signage exposure)
- Late fee and enforcement steps

## 2) Waterfall cash protection (investor term)
If using a quarterly revenue-share repayment, add a **minimum cash buffer covenant** so payments do not force operational negative cash.

Example wording (conceptual):
- Quarterly payment = min(revenue_share_amount, max(0, cash_end_before_payment − min_cash_buffer))

Reference:
- `investor_relations.md` (Risk Buffers)

## 3) Collections discipline
- Require withholding tax certificate (50 Tawi) within a defined timeline.
- Keep a tight aging report and escalations for juristic/committee approvals.

## 4) Operational buffers
- Maintain a small cash buffer specifically for quarter-end payout months.
- Prefer clusters where payment behavior is stronger (developer-managed portfolios) until the route reaches stable positive cash.


