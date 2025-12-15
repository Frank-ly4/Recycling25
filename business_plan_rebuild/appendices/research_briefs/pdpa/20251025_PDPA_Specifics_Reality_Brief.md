# PDPA Specifics Reality Brief

Date: 2025-10-24
Version: 1.0

## 1. Objective
To verify key requirements of Thailand's Personal Data Protection Act (PDPA) to inform the finalization of our compliance documents, specifically regarding the Data Protection Officer (DPO), privacy notices, and consent.

## 2. Desk Research Findings

| Requirement | Source | Finding | Implication for Our Plan |
| :--- | :--- | :--- | :--- |
| **Data Protection Officer (DPO)** | PDPC Thailand Guidelines | A DPO is mandatory if the "core activity" requires "regular and systematic monitoring of data subjects on a large scale." While "large scale" is not explicitly defined, it's a best practice for a B2C service that will scale. The DPO can be an internal staff member or an external service. | We must appoint a DPO. For the initial phase, the Operations Manager can be assigned this role with appropriate training. We need to explicitly name this person in our policy. |
| **DPO Contact Information** | PDPA, Section 37 | The name, address, phone number, and email address of the DPO must be made available to data subjects and the PDPC. This is typically done within the Privacy Notice. | The `31_PDPA_Compliance_Policy.md` must be updated with a dedicated, named DPO and their real contact details (e.g., a `privacy@company.com` email address). |
| **Privacy Notice** | PDPA, Section 23 | A privacy notice must be provided to data subjects *before or at the time of collection*. It must be clear, concise, and in easily accessible form. | We need to create a customer-facing Privacy Notice (in both Thai and English) and ensure it's provided to the Juristic Office to distribute to residents *before* our service begins. |
| **Legal Basis for Processing** | PDPA, Section 24 | For non-sensitive data (name, address, unit number for service delivery), we can rely on "contractual necessity" as the legal basis for processing, rather than explicit consent from every resident. | This simplifies our process. We don't need an "I agree" checkbox from every resident, as long as our service is part of the building's contract. However, our Privacy Notice must still be provided. |
| **Data Processing Agreements (DPAs)** | PDPA, Section 40 | As a Data Controller, we must have a written agreement with any third parties that process data on our behalf (e.g., a cloud provider, a software vendor). | We must create a DPA template and have it signed with any relevant vendors (e.g., our accounting software, cloud storage provider) before sharing any personal data. |

## 3. Triangulation & Analysis

*   **Immediate Action Required:** The PDPA requirements are not optional. We must have a named DPO and a public-facing privacy notice before we collect any data from our first pilot building.
*   **Simplification:** The "contractual necessity" basis simplifies our rollout, as we don't need to chase individual resident consent forms. This is a significant operational advantage.
*   **Gap in Documents:** Our current `legal_gap_list.md` correctly identifies the need to finalize the PDPA policy. This research provides the specific, actionable steps to do so. Our document set is missing a customer-facing Privacy Notice and a DPA template.

## 4. Conclusion & Recommendation

The research provides a clear, actionable checklist for achieving baseline PDPA compliance before launch.

**Recommendations:**
1.  **Appoint DPO:** Officially assign the DPO role to the Operations Manager in `appendices/_archive_reference_only/ops_playbooks/hiring_plan.md` (reference copy) and in `pdpa/PDPA_Compliance_Policy.md`.
2.  **Update PDPA Policy:** Replace the `[TO BE APPOINTED]` placeholders in the policy with the DPO's name, a business address, a dedicated phone line/extension, and a dedicated email address.
3.  **Create New Artifacts:**
    *   Create `pdpa/Privacy_Notice_EN_TH.md`: A bilingual, customer-facing document explaining our data practices.
    *   Create `pdpa/Data_Processing_Agreement_Template.md`: A template to use with our vendors.
4.  **Update internal checklist:** Track completion in `evidence_register.json` and ensure all PDPA artifacts are present before collecting any resident-level data.

This provides a clear path to ensuring our data handling practices are compliant from day one.
