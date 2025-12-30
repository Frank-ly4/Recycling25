# Foreign Ownership Restrictions Research (Thailand)

**Document Date:** 2025-12-30  
**Prepared by:** Legal/Compliance Lead  
**Purpose:** Evidence artifact documenting Thai Foreign Business Act restrictions and implications for equity structure

## 1. Executive Summary

Under Thailand's Foreign Business Act B.E. 2542 (1999), **service businesses** (including waste collection and environmental services) are classified as **List 3 restricted activities** requiring **≥51% Thai ownership** unless exempted via BOI promotion or specific ministerial approval.

**Implication for Recycling25:** Equity investments from foreign persons/entities must maintain aggregate foreign ownership ≤49%, OR company must obtain BOI promotion under Activity 5.1 (recycling/waste treatment) to allow 100% foreign ownership.

## 2. Legal Framework

### 2.1 Foreign Business Act (FBA) — Legislative Authority
- **Statute:** Foreign Business Act B.E. 2542 (1999)
- **Regulatory authority:** Ministry of Commerce, Department of Business Development (DBD)
- **Enforcement:** DBD audits shareholder registers; violations result in license revocation, fines, and potential criminal penalties

### 2.2 Three Lists of Restricted Businesses
| List | Restriction Level | Approval Authority | Examples |
|---|---|---|---|
| **List 1** | Prohibited (0% foreign) | No approval possible | Rice farming, land trading, newspapers |
| **List 2** | Restricted (case-by-case) | Cabinet or Minister approval | Domestic transport, rice milling, mining |
| **List 3** | Reserved for Thai nationals (unless licensed) | Ministry of Commerce license | Services, construction, retail <400M THB capital |

### 2.3 Definition of "Foreign Person" (FBA Section 4)
A **foreign person** includes:
1. Natural person without Thai nationality
2. Juristic person incorporated abroad
3. **Juristic person incorporated in Thailand** with:
   - ≥50% foreign shareholding (direct or indirect), OR
   - ≥50% foreign capital contribution, OR
   - Foreign persons holding >50% voting control

**Key implication:** A Thai-registered company with >50% foreign shareholders is treated as a "foreign person" for FBA purposes.

## 3. Service Business Classification (List 3)

### 3.1 List 3 Categories Relevant to Recycling25
From **Foreign Business Act, Annex 3:**

**Item 7: Services not otherwise specified in List 1 or List 2**
- General services (professional services, consulting, technical services)
- Environmental services and waste management (not explicitly named but falls under "services")

**Item 9: Brokerage, agency, or intermediary services**
- If company acts as intermediary between waste generators and processors

**Item 12: Accounting, legal, or other professional services**
- Not directly relevant but shows breadth of List 3 coverage

**Official interpretation:** DBD and Ministry of Natural Resources & Environment (MNRE) guidance treats **waste collection services** as List 3 restricted activity (confirmed via informal consultation; written guidance pending).

### 3.2 License Requirement for Foreign Persons
Foreign persons wishing to operate List 3 businesses must:
1. Apply for **Foreign Business License (FBL)** from Department of Business Development
2. Demonstrate "benefit to Thailand" (technology transfer, employment, export revenue, etc.)
3. Obtain approval from relevant regulatory bodies (BMA, MNRE for waste businesses)
4. Maintain minimum registered capital (1M-3M THB depending on activity)

**Practical reality:** FBL approval for service businesses is **difficult and slow** (6-18 months typical); most companies avoid by maintaining Thai majority.

## 4. Compliance Options for Equity Financing

### 4.1 Option 1: Thai-Majority Structure (Standard Path)
**Requirement:** Maintain ≥51% Thai shareholder ownership at all times.

**Pros:**
- No FBL application required
- No ongoing FBA compliance reporting
- Standard structure for service businesses in Thailand

**Cons:**
- Limits foreign investor participation to 49% aggregate
- May deter foreign VCs or impact valuation
- Requires careful UBO tracking (Thai entities with >50% foreign ownership counted as foreign)

**Implementation:**
- Shareholder Agreement must include Thai-majority maintenance covenant
- Any equity issuance/transfer requires FBA compliance check before board approval
- Quarterly cap table review to confirm 51% Thai threshold

### 4.2 Option 2: BOI Promotion (Foreign-Friendly Path)
**BOI exemption:** Companies promoted under **Board of Investment (BOI) Activity 5.1** (Recycling and Disposal of Waste and Scrap) are **exempt from Foreign Business Act restrictions** (Investment Promotion Act B.E. 2520, Section 16).

**Pros:**
- 100% foreign ownership permitted
- 8-year Corporate Income Tax (CIT) exemption (typical for Activity 5.1)
- Work permit and visa facilitation for foreign employees
- Duty-free import of machinery (if applicable)

**Cons:**
- Minimum investment thresholds (typically 1-10M THB depending on zone and technology level)
- Annual BOI reporting and compliance obligations
- Activity restrictions (must focus on promoted activity; side businesses require separate approval)
- Audit and inspection by BOI (annual or ad-hoc)

**Status:** BOI pathway decision documented in `audits/boi_decision_memo.md`.

### 4.3 Option 3: Revenue-Share Structure (Avoids FBA Entirely)
**Key insight:** Revenue-share agreements (debt-like instruments) do NOT constitute equity ownership and therefore are NOT subject to FBA restrictions.

**Rationale:**
- Revenue-share investor is a **creditor**, not shareholder
- No voting rights, board seats, or ownership transfer
- FBA regulates equity ownership in businesses, not debt/lending relationships

**Implication:** Company can raise capital from foreign investors via revenue-share (as documented in `investor_relations.md`) without FBA constraint. Equity remains optional/secondary structure.

## 5. Thai Law Sources & Precedents

### 5.1 Primary Statutes
- **Foreign Business Act B.E. 2542 (1999):** https://www.dbd.go.th/download/foreign_business_act.pdf
- **Foreign Business Act Ministerial Regulations:** Annex 1, 2, 3 (List 1/2/3 definitions)
- **Investment Promotion Act B.E. 2520 (1977, amended 2017):** BOI authority and exemptions

### 5.2 Regulatory Guidance
- **DBD Circular on "Foreign Person" Definition (2015):** Clarifies that Thai companies with >50% foreign UBO are treated as foreign
- **MNRE Guidance on Waste Business Licensing:** Cross-references FBA for foreign operators; confirms List 3 treatment

### 5.3 Case Precedents (Informal)
- **Service businesses commonly subject to FBA enforcement:** Consulting firms, logistics services, real estate agencies
- **Waste sector precedent:** No public case law; but informal DBD guidance confirms waste collection is List 3
- **Nominee shareholder cases:** Criminal penalties imposed on foreign persons using Thai nominees (FBA Section 36 violations)

## 6. Compliance Monitoring & Controls

### 6.1 Shareholder Register Tracking
- **Source of truth:** Official Thai company shareholder register (maintained by company secretary)
- **Nationality tracking:** Cap table (`cap_table.md`) must include "Nationality" column for each shareholder
- **UBO disclosure:** For any Thai entity shareholder, confirm ultimate beneficial ownership to determine if >50% foreign-owned (and thus "foreign person" for FBA purposes)

### 6.2 Pre-Investment FBA Compliance Check
Before any equity issuance or transfer:
1. Identify investor nationality/domicile
2. If foreign, calculate post-investment aggregate foreign ownership
3. If ≥50%, transaction breaches FBA unless:
   - Company obtains FBL (not recommended; slow and uncertain), OR
   - Company has BOI promotion (exempts from FBA), OR
   - Transaction is restructured as revenue-share/debt (not equity)

### 6.3 Quarterly Reconciliation
- **Trigger:** Every quarter, Finance Lead reviews shareholder register and confirms Thai-majority compliance
- **Red flag threshold:** If foreign ownership >45%, raise alert and restrict further foreign share transfers
- **Board reporting:** Include FBA compliance statement in quarterly board pack

### 6.4 SHA Covenant Language
Standard Shareholder Agreement clause (counsel-drafted):

> **Foreign Business Act Compliance:** The Company and all Shareholders acknowledge that the Company is subject to the Foreign Business Act B.E. 2542 (1999) and must maintain at least 51% Thai ownership unless exempted via BOI promotion. No Shareholder may transfer shares, and the Company may not issue new shares, if such transaction would result in aggregate foreign ownership exceeding 49% of issued shares, unless (i) the Company obtains a Foreign Business License, or (ii) the Company has obtained BOI promotion exempting it from FBA restrictions, or (iii) such transfer/issuance is approved by unanimous Shareholder consent.

## 7. Risk Assessment

### 7.1 Enforcement Risk
- **Likelihood:** Moderate. DBD conducts periodic audits of registered companies; service businesses are on watch list.
- **Detection mechanism:** Annual company filings (Form BorOrJor 5) require disclosure of foreign shareholders; DBD cross-checks against FBA compliance.
- **Trigger events:** Foreign investor seeking work permit, regulatory license applications, customer due diligence (if serving government/SOEs).

### 7.2 Penalties for Non-Compliance
Per FBA Section 33-36:
- **Operating without FBL (if >50% foreign and no exemption):** Up to 3 years imprisonment and/or fine up to 100,000 THB
- **Continued operation after warning:** License revocation, business closure order
- **Nominee arrangements (Section 36):** Criminal penalties for foreign person AND Thai nominee (both can face imprisonment)

### 7.3 Mitigation Strategies
1. **Maintain Thai-majority:** Safest and most common approach for service businesses
2. **BOI exemption:** If foreign ownership flexibility is critical, pursue BOI promotion
3. **Revenue-share primary structure:** Use revenue-share as main investment vehicle; offer equity as secondary/optional
4. **Legal review:** Engage Thai counsel to review SHA, cap table, and FBA compliance before any equity transaction

## 8. Recommendations

### 8.1 For Equity Structure (If Chosen)
1. **Default to Thai-majority:** Unless strong foreign investor demand and BOI pathway is viable
2. **Cap foreign ownership at 45%:** Build 6% buffer below 49% threshold for safety
3. **SHA compliance clause:** Include FBA maintenance covenant in all shareholder agreements
4. **Quarterly monitoring:** Finance Lead tracks and reports FBA compliance status

### 8.2 For Revenue-Share Structure (Recommended)
1. **Primary structure:** Use revenue-share as main investment vehicle (see `investor_relations.md`)
2. **FBA avoidance:** Revenue-share is debt, not equity, and thus not subject to FBA
3. **Equity as secondary:** Offer equity option for investors who require it, but structure as minority (<49%) or obtain BOI exemption

### 8.3 Next Steps
- [ ] Confirm current shareholder register (Gap ID: CC-01, FIELD item)
- [ ] If any foreign shareholders exist, calculate current foreign ownership %
- [ ] Decide BOI pathway (see `audits/boi_decision_memo.md`)
- [ ] Engage Thai counsel to draft SHA with FBA compliance clause

## 9. Sources & Citations

### 9.1 Statutes (Official English Translations)
- Foreign Business Act B.E. 2542 (1999), available at: https://www.dbd.go.th/download/foreign_business_act.pdf
- Investment Promotion Act B.E. 2520 (1977), available at: https://www.boi.go.th/index.php?page=law_detail

### 9.2 Regulatory Bodies
- **Department of Business Development (DBD):** https://www.dbd.go.th (foreign business licensing authority)
- **Board of Investment (BOI):** https://www.boi.go.th (promotion and FBA exemptions)

### 9.3 Legal Commentary
- **Baker McKenzie Thailand:** "Foreign Business Act Overview" (2023)
- **Tilleke & Gibbins:** "Foreign Ownership Restrictions in Thailand Service Sector" (2024)
- **Siam Premier International Law Office:** Informal consultation on waste service classification (December 2024)

## 10. Approval & Review

**Prepared by:** Legal/Compliance Lead  
**Reviewed by:** Business Owner / Founder  
**Next review date:** Quarterly or upon any equity transaction

---

**Audit Trail:**
| Date | Event | Updated By |
|---|---|---|
| 2025-12-30 | Initial FBA research and compliance analysis | Legal/Compliance Lead |

