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

**Template to request written guidance:** `audits/templates/DLT_WRITTEN_QUERY_TEMPLATE.md`

**Template to document district permit filings (if no online guidance):** `audits/templates/BMA_DISTRICT_PERMIT_FIELD_MEMO_TEMPLATE.md`

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

### 5.1 PDPA operational checklist (pilot-ready)
- **Before pilot start**:
    - Confirm DPO contact details are filled in `pdpa/PDPA_Compliance_Policy.md`.
    - Provide `pdpa/Privacy_Notice_EN_TH.md` to the juristic office for distribution/availability.
    - Identify any vendors who will process personal data (cloud drive, CRM, accounting) and execute `pdpa/Data_Processing_Agreement_Template.md` (or vendor DPA equivalent).
- **During operations**:
    - Avoid collecting resident identifiers by default (names/room numbers).
    - Avoid capturing faces in photos; if incidental capture occurs, restrict access and retain only as long as needed for proof/incident resolution.
    - Restrict access to operational logs and photos (role-based).
- **Retention**:
    - Keep tax/accounting records per statutory requirements; purge operational photos/logs when no longer needed for SLA/audit/claims.

## 6. Foreign Ownership Restrictions

### 6.1 Foreign Business Act (FBA) — Service Business Classification
**Authority:** Foreign Business Act B.E. 2542 (1999), List 3 — Service Businesses Reserved for Thai Nationals

**Restriction:** Service businesses (including waste collection, environmental services, consulting) require **≥51% Thai ownership** unless exempted.

**Our situation:**
- **Business model:** B2B recyclables collection service (service fee charged to condos)
- **Classification:** Falls under List 3 service restrictions
- **Current structure:** TBD (pending shareholder register confirmation; see `cap_table.md`)

### 6.2 Implications for Equity Financing

#### Option 1: Thai-Majority Structure (Standard Path)
- **Requirement:** Maintain ≥51% Thai shareholder ownership at all times
- **Foreign investor cap:** Foreign persons/entities limited to 49% aggregate ownership
- **Enforcement:** Ministry of Commerce can audit shareholder register; violations result in license revocation and fines
- **Practical implication:** If raising from foreign investors, total foreign ownership (direct + indirect) cannot exceed 49%

**Compliance steps:**
1. Confirm current shareholder register shows ≥51% Thai ownership
2. Draft SHA with explicit foreign ownership cap (49% ceiling)
3. Include "Thai-majority maintenance" covenant in investment docs
4. Require board approval for any transfer that would breach 51% Thai threshold

#### Option 2: BOI Promotion Exemption (Foreign-Friendly Path)
- **BOI exemption:** Companies promoted under Board of Investment (BOI) Activity 5.1 (Recycling/Waste Treatment) are **exempt from Foreign Business Act restrictions**
- **Implication:** 100% foreign ownership permitted if BOI-promoted
- **Trade-offs:**
  - **Pros:** Flexibility for foreign investors; 8-year CIT exemption; work permit privileges
  - **Cons:** Compliance burden (annual BOI reporting, activity restrictions, minimum investment thresholds)

**Status:** BOI pathway decision documented in `audits/boi_decision_memo.md` (see also `legal_compliance.md` Section 7).

### 6.3 Revenue-Share Structure (Avoids FBA Entirely)
**Key insight:** Revenue-share agreements (as documented in `investor_relations.md`) are **debt-like instruments**, not equity. They do not trigger Foreign Business Act restrictions because:
- No ownership transfer occurs
- No voting rights granted
- Investor is a creditor, not shareholder

**Implication:** If using revenue-share as primary structure, foreign investors can participate without FBA constraint. Equity remains optional/secondary.

### 6.4 Nominee/Proxy Shareholder Risk (DO NOT PURSUE)
**Warning:** Some advisors suggest using Thai "nominee shareholders" (foreign investor funds Thai citizens to hold shares on their behalf). **This is illegal under FBA Section 36** and carries criminal penalties. We will not pursue nominee structures.

### 6.5 Foreign Investor Nationality Screening
For any prospective equity investor:
1. Confirm investor legal domicile (Thai entity vs foreign entity)
2. If Thai entity, confirm ultimate beneficial ownership (UBO) — if >50% foreign-owned, treated as foreign for FBA purposes
3. Aggregate all foreign ownership (existing + proposed) to ensure <49% threshold

### 6.6 Compliance Monitoring
- **Quarterly:** Finance Lead reviews shareholder register to confirm Thai-majority compliance
- **Pre-transfer:** Any share transfer requires board approval + Foreign Business Act compliance check
- **Annual:** Include FBA compliance statement in annual governance review

### 6.7 Link to Cap Table & Term Sheet
- **Cap table:** `cap_table.md` must track nationality of each shareholder
- **Term sheet:** `equity_terms_summary.md` Section 6 includes Foreign Business Act considerations
- **SHA clauses:** Shareholder Agreement must include Thai-majority maintenance covenant (counsel-drafted)

## 7. BOI Pathway Analysis

### 7.1 Decision Status
**As of 2025-12-30:** Recycling25 has decided **NOT to pursue Board of Investment (BOI) promotion at seed stage**.

**Full rationale:** See `audits/boi_decision_memo.md` for complete analysis.

### 7.2 BOI Activity 5.1 — Recycling and Disposal of Waste
**Eligibility:** Recycling25's business model (collection, sorting, baling of recyclable materials) is eligible for BOI promotion under **Activity 5.1** (Category 5: Environmental Services).

**Key BOI incentives:**
- 8-year Corporate Income Tax (CIT) exemption
- 100% foreign ownership permitted (exempt from Foreign Business Act)
- Streamlined work permits/visas for foreign employees
- Import duty exemption on machinery/equipment

### 7.3 Why We Chose Not to Pursue BOI (Seed Stage)
**Primary reasons:**
1. **Net benefit modest (~1.2M THB over 8 years)** vs upfront cost + administrative burden
2. **Foreign ownership flexibility not needed:** Revenue-share structure (primary investment vehicle) is not subject to Foreign Business Act; equity is secondary
3. **Activity restrictions limit pivot flexibility:** BOI locks company into recycling activity; premature during pilot/validation phase
4. **Minimum investment threshold:** Bangkok Zone 1-2 requires 1-3M THB capex; our plan (~950k) is below threshold
5. **Founder time better spent on growth:** 30-50 hours/year BOI compliance vs customer acquisition, fundraising, operations

### 7.4 Alternative: Thai-Majority Structure
**Our approach:**
- Maintain ≥51% Thai shareholder ownership (Foreign Business Act compliant without BOI)
- Use revenue-share as primary investment structure (see `investor_relations.md`)
- Offer equity as secondary option (foreign ownership capped at 49%)
- Full operational and pivot flexibility; no BOI reporting burden

### 7.5 Revisit Triggers
We will reassess BOI promotion if:
- **Series A raise (≥10M THB):** Tax savings become material (~400k/year at 2M profit)
- **Foreign VC requires >49% ownership:** BOI exemption allows 100% foreign ownership
- **Capital-intensive expansion:** If machinery imports or large facility investment planned
- **Business model stabilizes:** Once past pilot phase with proven model (reduced pivot risk)

### 7.6 Compliance Implications
**Current structure:** Thai-majority (≥51% Thai ownership required; see Section 6 "Foreign Ownership Restrictions")

**Monitoring:**
- Quarterly cap table review to confirm Thai-majority compliance
- Foreign investor screening (confirm <49% aggregate foreign ownership)
- SHA includes Thai-majority maintenance covenant

**Documentation:**
- BOI decision memo: `audits/boi_decision_memo.md`
- BOI Activity 5.1 extract: `evidence/boi/20251230_boi_activity_5_1_extract.md`

## 8. Risk of Non-Compliance
*   **BMA Fine:** Up to 50,000 THB and/or imprisonment for operating without a license.
*   **DLT Fine:** Impounding of vehicle if used commercially without proper registration.
*   **Contractual:** Immediate termination if insurance or permits lapse.
