# Evidence Folder (Sources)

## Purpose
`business_plan_rebuild/` is intended to be shared as a standalone investor data room. The `evidence/` folder stores **source documents** (PDFs, screenshots, archived pages) that back material claims in the plan.

## How to Use
Each evidence item should be referenced from `evidence_register.json` with:
- `source_url`
- `local_path`
- `excerpt`
- `retrieved_at`

## Naming Convention
- `YYYYMMDD_source_topic_shorttitle.pdf`
- `YYYYMMDD_source_topic_shorttitle.png`
- `YYYYMMDD_source_topic_shorttitle.md` (for extracted text/notes)

## Priority Evidence (Top 10)
1. BMA waste fee ordinance / fee schedule for separation vs mixed waste.
2. Public Health Act B.E. 2535 (Section 31) licensing authority.
3. District office guidance for “Business Detrimental to Health” permits.
4. DLT rules for Yellow Plate and operator licensing for commercial transport.
   - Collected: `evidence/dlt/20251214_dlt_etl_user_manual_public.pdf` and `evidence/dlt/20251214_prd_dlt_e_transport_license_type70.html` (operator-license workflow for truck categories incl. type 70/80).
   - Still needed to fully close CLAIM-DLT-YELLOW-001: explicit DLT guidance (or written confirmation email/letter from the relevant Provincial Transport Office) mapping **our exact service model** to the required **plate class (yellow/public truck)** + **operator license**.
5. Revenue Department references for VAT registration threshold and WHT treatment.
6. Social Security employer contribution rules.
7. Bangkok truck restriction windows (surface roads).
   - Collected (Royal Gazette PDF via Parliament digital library): `evidence/royal_thai_police/20251214_odl_truck_ban_bkk_4_6_wheel_2552.pdf` (Bangkok ban windows 06:00–09:00 and 16:00–20:00 for 4-wheel and 6-wheel trucks, except public holidays).
8. Current Bangkok wage benchmarks (driver/loader/sorter).
9. Fleet lease quotes (Siam Rajathanee / Krungthai Car Rent) for pickup + NPR.
10. Warehouse rental comps (Phra Khanong / On Nut).
