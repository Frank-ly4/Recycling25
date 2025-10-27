# Facility Rent Reality Brief

Date: 2025-10-24
Version: 1.0

## 1. Objective
To validate the facility rent assumption in `finance/assumptions.md` and `ops/facility_plan.md` with current market data for Bangkok.

## 2. Desk Research Findings

| Property Type | Source | Location | Size | Price (THB/sqm/month) | Total Monthly Rent (THB) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Warehouse/Light Industrial | CBRE / Plus Property / Hipflat (Oct 2025 listings) | Phra Khanong, Suan Luang (near On Nut) | 150-250 sqm | 150 - 200 | 22,500 - 50,000 |
| Small Warehouse | Local Real Estate Listings | Lat Phrao, Bang Kapi | 150-200 sqm | 140 - 180 | 21,000 - 36,000 |
| Converted Shophouse (Ground Floor) | Fazwaz Property Listings | Outer Sukhumvit | ~120-160 sqm | 160 - 220 | 19,200 - 35,200 |

## 3. Triangulation & Analysis

*   **Market Rate:** The consistent market rate for a suitable 150 m² facility in our target operational zones is **150-200 THB/sqm**.
*   **Realistic Budget:** This puts a realistic monthly rent in the range of **22,500 - 30,000 THB**.
*   **Comparison to Financial Model:** Our current model assumes a rent of **20,000 THB/month**. This is below the low end of the market range and should be considered a high-risk assumption. While a deal at this price might be possible for an older property requiring renovation, it's not a reliable baseline.

## 4. Conclusion & Recommendation

The research indicates our facility rent assumption is too optimistic.

**Recommendations:**
1.  **Update `finance/assumptions.md`:** Adjust the "Facility rent" line item in the Base Monthly OPEX from 20,000 THB to a more realistic **25,000 THB**.
2.  **Update `finance/financial_model.csv`:** Recalculate the `fixed_opex_THB` and `net_profit_THB` columns to reflect this 5,000 THB monthly increase. This will slightly delay the break-even point but creates a more robust and defensible plan.
3.  **Update `ops/facility_plan.md`:** Update the rent ranges in the OPEX section to reflect the 150-200 THB/sqm finding.
4.  **Add Citation:** Cite this brief in all updated documents.

This adjustment reduces risk in our financial projections and aligns them with current market reality.

