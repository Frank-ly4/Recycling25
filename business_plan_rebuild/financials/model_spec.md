# Financial Model Spec (Investor-Grade)

## 1. Purpose
This document defines the accounting and modeling logic used to generate:
- `projections.json` (P&L-like monthly view)
- `cashflow.json` (cash movement + balances)
- `waterfall.json` (investor repayment schedule)

All outputs are generated from a single source of truth: `model_inputs.json`.

## 2. Definitions
- **Revenue (service)**: Units Ã— Fee per unit per month (exclusive of VAT).
- **Units**: Buildings Ã— Units per building.
- **Variable costs**: Units Ã— Variable cost per unit.
- **Fuel**: Base fuel + step increments based on building count.
- **Direct labor**: Driver + Loader + Sorter (Sorter begins at `sorter_start_month`).
- **Admin**: Ops manager salary.
- **Fixed**: Facility rent + vehicle lease + rescue budget + misc contingency.

## 3. Taxes & Cash Policy
- **VAT**: Outputs are exclusive of VAT (modeled as pass-through).
- **Withholding tax (WHT)**: Cash receipts reduced by WHT (default 3%); treated as receivable/credit (not an expense).
- **Corporate income tax**: Simplified monthly tax = max(0, pre-tax profit) Ã— tax rate (real-world is annual).
- **Collections**: Net-30 assumed (cash collected 1 month after invoice).

## 4. Investor Waterfall
- **Type**: Revenue share with cap.
- **Mechanism**: At each quarter-end month (3,6,9,12,...), pay `revenue_share_pct` Ã— (sum of service revenue for that quarter), until cumulative payments reach cap = principal Ã— cap_multiple.

## 5. One-Time Cash Costs
One-time cash costs (deposits, bins/signage, permits setup) are cash outflows in their specified month and do not appear as recurring P&L expenses.

## 6. Validation Rules (Must Pass)
- Starting cash in inputs equals Month-0 cash in `cashflow.json`.
- Re-running generator yields identical output given identical inputs.
- `waterfall.json` matches repayment terms in `investor_relations.md`.
