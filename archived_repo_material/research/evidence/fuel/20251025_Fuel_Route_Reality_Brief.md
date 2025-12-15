# Fuel & Route Reality Brief

Date: 2025-10-24
Version: 1.0

## 1. Objective
To validate the fuel cost assumptions in `finance/assumptions.md` by verifying three key inputs: diesel price, vehicle fuel efficiency, and estimated daily route distance.

## 2. Desk Research Findings

| Data Point | Source | Finding | Value / Range |
| :--- | :--- | :--- | :--- |
| **Diesel Price** | PTT Public Price (Oct 2025) | The retail price for diesel in Bangkok has been stable. | **32-34 THB/liter** |
| **Vehicle Fuel Efficiency** | Isuzu Specs / Fleet Owner Forums | The Isuzu N-Series (NPR) is rated for ~6-8 km/L on highways. However, for stop-and-go city driving with a full load, fleet operators report a real-world efficiency of **4-5 km/L**. | **4.5 km/L** (conservative average) |
| **Estimated Route Distance** | Google Maps Route Simulation | A sample route starting from a Phra Khanong facility, servicing 4 large condos in the Watthana/Khlong Toei area, and returning, is approximately **25-35 km**. A full day might involve two such routes or one larger, less dense route. | **60-80 km** per operational day |

## 3. Triangulation & Analysis

*   **Daily Fuel Consumption:**
    *   Distance: 70 km (midpoint of daily estimate)
    *   Efficiency: 4.5 km/L
    *   **Fuel Used:** 70 km / 4.5 km/L = **~15.5 liters/day**

*   **Monthly Fuel Cost (per vehicle):**
    *   Operational Days: 22 days/month (assuming Mon-Fri with some Saturdays)
    *   Total Liters: 15.5 liters/day * 22 days = **341 liters/month**
    *   Price per Liter: 33 THB (midpoint)
    *   **Total Monthly Cost:** 341 liters * 33 THB/L = **~11,253 THB/month**

*   **Comparison to Financial Model:**
    *   The `finance/assumptions.md` file budgets for fuel within the "Collection costs" variable cost, allocating 6 THB per unit.
    *   In Month 5, with 2,000 units (5 buildings), the model allocates: 2,000 units * 6 THB/unit = **12,000 THB** for fuel.
    *   Our bottom-up research estimates the cost at **~11,253 THB**.

## 4. Conclusion & Recommendation

The research **validates the fuel cost allocation in the financial model as accurate and slightly conservative.**

*   The 6 THB per unit allocation is a reliable proxy for fuel costs, scaling correctly with the number of customers.
*   The original assumption of `4 km/liter efficiency` and `35 THB/liter` was a safe, conservative estimate that resulted in a correct budget, even if the real-world numbers are slightly different.

**Recommendations:**
1.  **Update `finance/assumptions.md`:** Replace the original fuel source note with a citation to this brief. The sentence can be updated to:
    *   "Source: Fuel costs are based on a bottom-up calculation of ~11,253 THB/month for a fully utilized vehicle (see `research/evidence/fuel/20251025_Fuel_Route_Reality_Brief.md`), which aligns with the 6 THB/unit variable cost allocation."
2.  **No changes to the financial model (`.csv`) are required.** The existing allocation is sound.

This research confirms our fuel cost projections are realistic for Bangkok operations.
