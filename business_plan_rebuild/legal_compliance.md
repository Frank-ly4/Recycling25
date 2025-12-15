# Legal & Compliance Framework

## 1. Regulatory Permits (Thailand)

### 1.1. Bangkok Metropolitan Administration (BMA)
*   **Permit Type:** "License for Operation of Business Detrimental to Health" (กิจการที่เป็นอันตรายต่อสุขภาพ).
*   **Authority:** Public Health Act B.E. 2535 (1992), Section 31. <!-- claim:CLAIM-BMA-LICENSE-001 -->
*   **Specific Category:** Type 9 (Business related to hygiene or environment) - Waste Collection/Transport.
*   **Application Form:** **Form Sor.Por. 1 (แบบ สภ.1)**. <!-- claim:CLAIM-BMA-LICENSE-001 -->
*   **Filing Location:** Environmental Sanitation Section (ฝ่ายสิ่งแวดล้อมและสุขาภิบาล) at the local District Office (Khet) where the warehouse is located.
*   **Estimated Fee:** ~5,000 - 10,000 THB/year (varies by facility size/horsepower).
*   **Requirement:** Approved facility inspection (sanitation, ventilation, pest control).
*   **Status:** **MANDATORY** before commercial operation.

### 1.2. Department of Land Transport (DLT)
*   **Vehicle Registration:** **Commercial Transport License (Yellow Plate 70-xxxx)**. <!-- claim:CLAIM-DLT-YELLOW-001 -->
    *   *Authority:* Land Transport Act B.E. 2522 (1979).
    *   *Rationale:* DLT’s published plate/registration rules define non-scheduled truck transport with a yellow-background plate and number ranges including **70–79** (see `business_plan_rebuild/evidence/dlt/20251214_dlt_royal_gazette_plate_numbers_trucks_2565.pdf`). **ASSUMPTION—VALIDATE:** whether our specific service model (recyclables pickup + service fee) is treated as non-scheduled transport-for-hire (and therefore requires the relevant registration/operator licensing) still requires explicit DLT guidance or written confirmation. <!-- claim:CLAIM-DLT-YELLOW-001 -->
*   **Driver License:** Type 2 (Commercial) Driving License (ใบขับขี่ บ.2) required for all drivers.
*   **Constraint:** Yellow plate registration requires the company to have a transport permit license number (significant paperwork hurdle).
*   **Mitigation:** **Lease via Licensed Partner** (License Bridge). The lessor (e.g., Siam Rajathanee) holds the operator license and plates; we operate as the client.

#### 1.2.1 License Bridge — execution checklist (Bangkok-feasible)
During Months 1–6 (or until our own operator licensing is confirmed), run transport under the licensed lessor/operator and keep the following available for inspections/site checks:
* **On-truck packet:** lease agreement excerpt showing operator/vehicle details, commercial insurance certificate, vehicle registration/plate, driver license class (commercial), and a copy of the service agreement scope.
* **Operational logs:** pickup schedule, time-in/time-out logs, and a basic manifest/route sheet consistent with our chain-of-custody approach.

#### 1.2.2 Close the remaining classification risk (CLAIM-DLT-YELLOW-001)
We will obtain **explicit written guidance/confirmation** from the relevant DLT office for our exact service model (“recyclables pickup + service fee + chain-of-custody reporting”), and store the response in `evidence/` to close this claim.

### 1.3. Factory Act (Department of Industrial Works)
*   **Threshold:** Machinery < 50 HP and < 50 workers.
*   **Plan:** Keep sorting facility below these thresholds to avoid full Factory License (Ror.Ngor.4) requirements.
*   **Equipment Cap:** Use vertical balers (typically 5-10 HP) to stay safely under the 50 HP aggregate limit.

## 2. Tax & Revenue Code Compliance
*   **VAT (Value Added Tax):**
    *   *Threshold:* Mandatory registration if revenue > 1.8M THB/year (Revenue Code Sec. 81/1). <!-- claim:CLAIM-VAT-THRESH-001 -->
    *   *Rate:* 7%.
    *   *Implication:* All contracts must be VAT-exclusive.
*   **Withholding Tax (WHT):**
    *   *Service Income:* 3% WHT (Revenue Code Sec. 3 Tre). <!-- claim:CLAIM-WHT-SVC-001 -->
    *   *Transport Income:* 1% WHT (if registered as transport operator).
    *   *Cash Flow:* We assume 3% deduction on receipts.

## 3. Corporate Structure & Labor
*   **Entity:** Thai Limited Company (51% Thai owned) to avoid Foreign Business Act restrictions on service businesses (List 3).
*   **Social Security:** Mandatory registration for all full-time employees (Driver, Loader, Sorter) under Section 33.
*   **Safety (OSHA equivalent):** Provision of PPE (gloves, masks, boots) and H&S training logs required by Labor Protection Act.

## 4. Condo Service Agreements
*   **Contract Type:** B2B Service Agreement (Company to Juristic Person).
*   **Key Clauses:**
    *   **Scope:** Defined recyclables (PET, HDPE, Cans, etc.).
    *   **Exclusions:** Hazardous waste, wet waste, construction debris.
    *   **Indemnity:** Provider not liable for pre-existing bin room conditions; Client liable for hazardous items placed in bins.
    *   **Term:** 12 months (auto-renew).
    *   **Payment:** Net 15 or Net 30 days.

## 5. Data Privacy (PDPA)
*   **Scope:** Juristic contact details are B2B, but any identifiable **Resident Data** (names/room numbers, face images) or **employee GPS/location data** falls under PDPA.
*   **Approach (Bangkok-feasible):** **Data minimization by default.** Operate building-level reporting without resident identities unless explicitly required by a client program.
    *   **Do collect:** timestamp, building/site ID, weights by material, contamination flags, pickup photos (avoid faces), invoice/admin contact details.
    *   **Avoid collecting:** resident names/room numbers and any unnecessary identifiers.
*   **Data room artifacts (standalone):**
    *   `pdpa/PDPA_Compliance_Policy.md` (internal policy framework)
    *   `pdpa/Privacy_Notice_EN_TH.md` (bilingual notice for distribution before any resident-level data collection)
    *   `pdpa/Data_Processing_Agreement_Template.md` (for cloud/accounting/CRM vendors)

## 6. Risk of Non-Compliance
*   **BMA Fine:** Up to 50,000 THB and/or imprisonment for operating without a license.
*   **DLT Fine:** Impounding of vehicle if used commercially without proper registration.
*   **Contractual:** Immediate termination if insurance or permits lapse.
