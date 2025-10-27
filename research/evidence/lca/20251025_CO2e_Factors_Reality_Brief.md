# CO2e Factors Reality Brief

Date: 2025-10-24
Version: 1.0

## 1. Objective
To find authoritative, Thailand- or ASEAN-specific Life Cycle Assessment (LCA) emission factors for recycled materials to replace the "illustrative" factors in `config/co2e_factors.json`.

## 2. Desk Research Findings

| Source Searched | Finding | Conclusion |
| :--- | :--- | :--- |
| **Thailand Greenhouse Gas Management Organization (TGO)** | TGO provides national and sector-specific emission factors, but primarily for energy, transport, and waste disposal (landfill, incineration). Specific factors for CO2e *avoided* by recycling PET, HDPE, paper, etc., are not readily available in their public database. | No direct replacement for our illustrative factors found. |
| **ASEAN Environmental Research Portals** | Academic studies on waste management in Southeast Asia exist, but a consolidated, peer-reviewed factor table for multiple recycled materials is not available through general search. | Sourcing these would require in-depth academic database research, which is beyond the scope of this verification sprint. |
| **International Databases (e.g., EPA, IPCC)** | Standard international factors (like those from the US EPA) are available and are often used as proxies when local data is absent. | Using international factors is a common and acceptable practice, provided the source is cited and the data is clearly marked as a proxy. |

## 3. Triangulation & Analysis

*   **Data Gap:** There is a clear data gap for localized, public CO2e *avoided* factors for recycling in Thailand.
*   **Risk of Inaccuracy:** Using our current "illustrative" factors without a clear source is a data integrity risk. Using international factors is better, as they are sourced, but they may not perfectly reflect the Thai energy mix and industrial processes.
*   **Path Forward:** The most responsible approach is to use a reputable international source, cite it clearly, and maintain the "estimate" language in all reporting.

## 4. Conclusion & Recommendation

We cannot replace the illustrative factors with official Thai/ASEAN factors at this time. We should, however, improve data integrity by adopting a reputable international standard as a placeholder.

**Recommendations:**
1.  **Update `config/co2e_factors.json`:** Replace the current illustrative factors with factors from a recognized international source (e.g., the US EPA's WARM model).
2.  **Add Versioning and Citation:** Update the JSON to `v20251025-INTL` and add a `source` field with the URL to the international database.
3.  **Update ESG Template:** Modify the footnote in `docs/GoToMarket/07_ESG_Report_Template.md` to state: "CO2e estimates are based on factors from the US EPA WARM model (vXX) as a proxy, pending availability of localized Thai/ASEAN LCA data."
4.  **Add to `VERIFICATION_PLAN.md`:** Add a long-term task to periodically re-scan for Thai-specific LCA studies.

This approach ensures transparency and improves the credibility of our ESG reporting, even with the existing data limitations.
