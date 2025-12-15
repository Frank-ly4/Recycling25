# Facility Rent Reality Brief

Date: 2025-10-24
Version: 1.0

## 1. Objective
To validate the facility rent assumptions used by the standalone data room and the execution facility plan for Bangkok.

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
1.  **Update canonical model inputs (if needed):** If the standalone model assumes facility rent below market, adjust `business_plan_rebuild/financials/model_inputs.json` `drivers.fixed_costs.facility_rent` toward **25,000–30,000 THB/month** for a 150m² facility at 150–200 THB/sqm.
2.  **Update facility plan references:** Ensure `appendices/ops_playbooks/facility_plan.md` rent ranges and citations reflect the 150–200 THB/sqm finding.
3.  **Add citation:** Cite this brief wherever facility rent is discussed.

This adjustment reduces risk in our financial projections and aligns them with current market reality.

