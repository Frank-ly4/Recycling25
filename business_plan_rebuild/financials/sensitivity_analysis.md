# Sensitivity Analysis

## 1. Variable Impact Summary
We tested the model against three critical variables: **Service Fee**, **Building Ramp Speed**, and **Fuel Costs**.

### Base Case vs. Scenarios (Month 12 Snapshot)
*   **Base Case:** 9 Buildings (3,600 units), 90 THB/unit.
    *   **Net Income (generated):** **16,800 THB/month** (EBITDA 21,000; tax_simplified 4,200). See `financials/projections.json`.
    *   **Cash (generated):** Month 12 cash_end = **38,160 THB** (after the Month 12 revenue-share payment). See `financials/cashflow.json`.

### Scenario A: Price Pressure (-10%)
*   **Condition:** Competition forces price down to 80 THB/unit.
*   **Impact:**
    *   Revenue decreases by 36,000 THB (3,600 units * 10 THB).
    *   **At Month 12 scale (9 buildings):** Net income flips negative (approx. **-15k THB/month**, tax ≈ 0) because fixed costs dominate early.
*   **Mitigation:** Maintain a pricing floor (≥85 THB/unit) or accelerate scale to ~12 buildings to restore ≥60k/month net income.

### Scenario B: Slow Ramp (Delay 3 months)
*   **Condition:** Reaching 9 buildings takes 15 months instead of 12.
*   **Impact:**
    *   Cash burn extends.
    *   At 6 buildings scale, the generated base case net income is still negative (Month 8: **-33,000 THB/month**), so a slow ramp materially increases runway risk.
*   **Buffer:** Seed capital (1.5M) provides runway, but the base case still dips to a **small temporary shortfall** (cash low point **Month 15: -23,040 THB**, per `cashflow.json`). This requires strict collections (advance billing / Net-15) and/or a small working-capital buffer.

### Scenario C: Fuel Spike (+20%)
*   **Condition:** Diesel prices rise significantly.
*   **Impact (Month 12 baseline):** Fuel rises from 12,000 to 14,400 (+2,400), reducing Month 12 net income from 16,800 to ~14,400 THB/month (tax decreases slightly).
*   **Resilience:** High. Fuel is a small % of OPEX compared to labor and fleet lease.

## 2. Break-Even Analysis
*   **Net Income Break-Even (generated base case):** **Month 12** at **9 buildings** (net income 16,800 THB).
*   **Profit Target (≥60k net income, generated base case):** **Month 15** at **~12 buildings** (net income 72,000 THB).

## 3. Recommendation
Maintain firm pricing floor at 85 THB/unit. If forced lower, require larger clusters (min 5 buildings) to reduce variable logistics costs.

