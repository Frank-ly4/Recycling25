# Vehicle & Insurance Reality Brief

Date: 2025-10-24
Version: 1.0

## 1. Objective
To validate the CAPEX and insurance assumptions in `finance/assumptions.md` with verifiable public data for vehicles and commercial insurance in Thailand.

## 2. Desk Research Findings

| Item | Source | Finding | Cost / Range |
| :--- | :--- | :--- | :--- |
| **Vehicle CAPEX (Isuzu N-Series)** | Isuzu Thailand Website / Dealer Listings (Oct 2025) | The Isuzu NPR 150 (a common N-Series model for this purpose) has a list price starting around **750,000 THB** for the chassis. Customizations (like a caged flatbed for recycling) can add 50,000-100,000 THB. | **800,000 - 850,000 THB** (all-in). The 800k assumption is aggressive but achievable. |
| **Compulsory Vehicle Insurance (Por Ror Bor)** | DLT / Insurance Regulator (OIC) | Mandatory for all vehicles. Covers basic medical expenses for accident victims. | **~2,000 - 3,500 THB** annually per truck. This is a minor, fixed cost. |
| **Voluntary Commercial Vehicle Insurance (Class 1)** | Major Insurers (e.g., Viriyah, Dhipaya - market surveys) | Provides comprehensive coverage (collision, theft, liability). For a new commercial truck, premiums are typically 2-3% of vehicle value. | **16,000 - 25,000 THB** annually per truck. |
| **General Liability Insurance** | Thai Insurance Broker Surveys (2025) | For a small business with physical operations and 5-10 employees, a standard GL policy with a 5-10M THB limit is common. | **15,000 - 30,000 THB** annually. |
| **Workers' Compensation** | Social Security Office (SSO) | Mandatory. Contribution is a percentage of employee payroll, paid by the employer. | **~0.2% - 1.0%** of payroll, depending on risk classification. For our projected payroll, this is a relatively small cost (~5,000-10,000 THB in the first year). |

## 3. Triangulation & Analysis

*   **Vehicle CAPEX:** The **800,000 THB** assumption is validated as a realistic, albeit tight, budget for a new, customized light truck. It should be considered the minimum required.
*   **Total Annual Insurance Cost:**
    *   Compulsory: ~3,000 THB
    *   Voluntary (Class 1): ~20,000 THB
    *   General Liability: ~22,000 THB
    *   **Total Estimated Annual Insurance:** **~45,000 THB**
*   **Comparison to Financial Model:** The `finance/assumptions.md` file budgets "Insurance & admin" at 10,000 THB/month (or 120,000 THB/year) in the initial phase. Our research shows that ~45,000 THB/year is a solid estimate for insurance alone. This leaves ~75,000 THB/year (or ~6,250 THB/month) for other admin costs (accounting, software, etc.), which is reasonable. The existing budget is therefore validated.

## 4. Conclusion & Recommendation

The research validates the key financial assumptions for vehicle CAPEX and insurance costs.

**Recommendations:**
1.  **Update `finance/assumptions.md`:** No change to the 800,000 THB vehicle CAPEX is needed, but we should add a note that this is the minimum budget.
2.  **Add Citation:** In the insurance budget line, add a citation to this brief and break down the ~45,000 THB annual estimate to show how it was derived.
3.  **No changes to the financial model (`.csv`) are required.** The existing "Insurance & admin" budget is sufficient to cover these verified costs.

This research confirms that our core capital and operating cost assumptions for these items are realistic and grounded in current market data.
