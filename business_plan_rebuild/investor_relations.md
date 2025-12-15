# Investor Relations & Repayment Plan

## 1. Investment Ask
**Total Funding Required:** 1,500,000 THB (Seed Tranche).

### Use of Funds
| Category | Amount (THB) | % | Details |
| :--- | :--- | :--- | :--- |
| **Fleet & Logistics** | 500,000 | 33% | Isuzu NPR Down Payment (25%), Insurance (Yellow Plate), Bins. |
| **Facility & Equip** | 450,000 | 30% | Warehouse Deposit (3mo), 20T Vertical Baler Down Payment. |
| **Working Capital** | 550,000 | 37% | 6-month Payroll Buffer, Fuel, Marketing, Legal Fees. |
| **TOTAL** | **1,500,000** | **100%** | |

## 2. Repayment Schedule (Waterfall)
We propose a **Revenue Share + Cap** model or **Straight Equity** depending on investor preference. Below is the **Debt/Rev-Share hybrid** structure for cash-flow focused investors.

*   **Structure:** 10% of Gross Revenue paid quarterly until 1.5x Cap is reached. <!-- claim:CLAIM-INVEST-TERMS-001 -->
*   **Cap:** 2,250,000 THB (1.5x on 1.5M).

### Projected Repayment Timeline
The figures below are **directly derived from the generated model outputs** (`financials/projections.json` for revenue and `financials/waterfall.json` for payments).

*   **Year 1 Service Revenue:** ~2.232M THB → **Payments:** 201,600 THB (Months 6/9/12).
*   **Year 2 Service Revenue:** ~5.688M THB → **Payments:** 568,800 THB (Months 15/18/21/24).
*   **Year 3 Service Revenue:** ~6.048M THB → **Payments:** 604,800 THB (Months 27/30/33/36).
*   **Year 4 Service Revenue:** ~6.048M THB → **Payments:** 604,800 THB (Months 39/42/45/48).
*   **Year 5 Service Revenue:** ~6.048M THB → **Payments:** 270,000 THB (Months 51/54; cap reached).
*   **Total Time:** **Cap reached at Month 54 (~4.5 years)**. See `financials/waterfall.json`.

## 3. Risk Buffers
1.  **Fees-First Model:** We do not rely on plastic trading margins to pay back investors. 100% of repayment comes from contracted service fees.
2.  **Cash Reserve (Execution Reality — Bangkok):** The generated base case is **tight in Year 1** and reaches a low point of **Month 15 cash_end = -23,040 THB** (timing driven by quarterly revenue-share payments). See `financials/cashflow.json`.
    *   **Mitigation A (contract terms, standard for B2B services):** **Advance billing + Net-15** + service suspension for arrears (see `outreach_kit/service_agreement_12m.md`). This improves cash timing versus the model’s conservative Net-30 assumption.
    *   **Mitigation B (common control):** **Security deposit / equipment deposit** (Schedule A) to reduce payment-delay risk and cover bins/signage exposure.
    *   **Mitigation C (investor-friendly but operations-safe):** Add a **minimum cash buffer covenant** to the waterfall so quarterly payments are the *lesser of* the revenue-share amount and available cash above a defined buffer (e.g., 100,000 THB). This avoids operational stoppage while preserving the agreed cap.
    *   **Mitigation D (structure option):** If an investor requires strict quarterly sweeps, shift the **first payment month** later (e.g., month 9) or use a lower % in Year 1, then step up after ≥9 buildings.
3.  **Asset Backing:** Bins and equipment retain liquidation value (~300k).

## 4. Reporting Cadence
*   **Monthly:** "Flash Report" (Revenue, Units, Cash Balance).
*   **Quarterly:** Full P&L + Repayment Transfer.
*   **Annual:** Audit & Strategy Review.
