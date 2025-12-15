# Operations Plan: High-Volume Logistics

## 1. Logistics Strategy: "Cluster Density"
To achieve profitability with 90 THB/unit fees, we must minimize "windshield time" (driving empty).

### 1.1. Pilot Cluster: "Phra Khanong - On Nut" (The 5km Loop)
We will launch strictly in the **Sukhumvit 71 (Pridi) to Sukhumvit 77 (On Nut)** corridor.
*   **Rationale:** High density of 300-600 unit condos (Mid-market), accessible truck routes, close to affordable warehouse space.
*   **Target Accounts (Sample):**
    1.  **The Line Sukhumvit 71** (~290 units) - *Anchor Tenant*.
    2.  **Wyne Sukhumvit** (~460 units) - *Volume Driver*.
    3.  **Aspire Sukhumvit 48** (~800 units) - *Major Hub*.
    4.  **The Base Sukhumvit 77** (~1,200 units) - *Mega Site (Requires bi-weekly pickup)*.
    5.  **Blocs 77** (~460 units).
*   **Constraint:** Accept new buildings ONLY within 5km of this core loop in Year 1.

### 1.2. Constraints & Ban Windows (Bangkok)
Routes must comply with Bangkok truck restriction windows on surface roads (Royal Gazette / traffic officer regulation). <!-- claim:CLAIM-TRUCK-BAN-001 -->
*   **06:00 – 09:00** (Morning Ban)
*   **16:00 – 20:00** (Evening Ban)
*   *Implication:* Pickups must occur in the **09:30 – 15:30** window or after 20:00 (Night shift). <!-- claim:CLAIM-TRUCK-BAN-001 -->

## 2. Collection Process (SOP)
1.  **Arrival:** Driver scans QR code at building dock (Time-in).
2.  **Loading:**
    *   Inspect bins for contamination (>15% = rejection/penalty).
    *   Weigh bags using portable scale; log weight in Driver App (or Log Sheet).
    *   Load into cage truck (segregated by material type if possible).
3.  **Departure:** Sign-off with Juristic Manager/Security. Scan QR (Time-out).
4.  **Handoff:** Deliver to consolidation facility for sorting/baling.

### 2.1 Execution SOP (condensed, canonical)
This section is the canonical “field SOP” for execution. It is intentionally short so it can be used as a daily checklist.

#### Collection SOP (Condo)
- Arrival and check-in with juristic/security; photo of bins/area
- Weigh per material category; log in app/form; label bags by condo/date
- Load by category into non-compacting truck; secure load; minimize dwell time
- Note contamination issues; leave replacement bags/bins as needed
- Departure confirmation; notify manager; capture any requests/issues

#### Sorting & Quality Control SOP
- PPE required; station brief; hazard screening
- Pre-separate PET (clear vs colored), HDPE, paper grades, metals, glass
- Remove contaminants; record estimated contamination rate
- Bale where applicable; store by material; maintain chain-of-custody logs
- Prepare weekly inventory for offtake pickup/delivery

#### Health & Safety and Crisis Communications (essentials)
- H&S: PPE list, lifting technique, vehicle/machine lockout, incident reporting
- Insurance: vehicle, public liability, workers’ comp — policy contacts
- Crisis comms: designated spokesperson, 60-min response window, channels (LINE, email), holding statements for service lapse, accident, contamination claim
- Evidence: photos, logs, GPS/fuel data; root-cause review within 72 hours

#### SLA measurement (on-time definition + reporting)
Purpose: Define how SLA metrics are measured, recorded, and reported for contracts and pilots.

On-time definition
- On-time is arrival within the scheduled 4-hour window agreed in Schedule B.
- Timestamps captured via driver app and photo metadata; fallback: security sign-in logs.

Data capture
- Required fields: building, route/date, planned window, arrival/departure, reason codes (delay, access, weather), photo proofs.
- Overflow detection: on-site observation with photos; resident/manager photo reports tagged and verified.

Exclusions
- Force Majeure, access denial, hazardous conditions, or Client-caused delays are excluded from on-time calculations.

Escalation & backup
- If a pickup is missed, notify Client within 24h with a revised window; target backup within 48h subject to access and resources.
- Document root cause; apply corrective actions.

Reporting
- Monthly SLA report: on-time %, missed pickups, reasons, credits (if any).
- Audit trail preserved 12 months.

## 3. The Fleet: "Mixed Strategy"
To handle variable dock heights and licensing lags, we employ a mixed fleet. <!-- claim:CLAIM-FLEET-MIX-001 -->

### 3.1. Vehicle Types
*   **Primary Unit:** **Isuzu NPR 150 (Yellow Plate)**
    *   *Role:* Main route, street-level loading.
    *   *Capacity:* 2,000 kg / 12m3.
    *   *Specs:* Height ~2.3m (Cannot enter most condo basements).
*   **Rescue Unit:** **Suzuki Carry / Toyota Hilux Standard (Modified Cage)**
    *   *Role:* Low-clearance basements (<2.1m) and "Feeder Runs".
    *   *Capacity:* 900 kg / 4m3.
    *   *Requirement:* Height < 1.9m (requires low-profile cage modification).

### 3.2. Acquisition Strategy (The "License Bridge")
*   **Months 1-6:** **Mandatory Lease/Rental**.
    *   *Partner:* **Siam Rajathanee** or **Krungthai Car Rent** (Fleet Management). <!-- claim:CLAIM-LEASE-PARTNER-001 -->
    *   *Reason:* Avoids 90-day delay for DLT Operator License. Includes maintenance and replacement truck.
    *   *Cost:* Premium over owning, but mitigates "No License" regulatory risk.
*   **Months 7+:** Evaluate purchasing own fleet once DLT Operator License is secured.

#### 3.2.1 License Bridge — field compliance packet (Bangkok)
For every route during the lease/rental bridge period, carry a simple “inspection packet” to reduce stoppage risk:
* Lease agreement excerpt showing the licensed operator/owner and vehicle details
* Commercial insurance certificate for the vehicle
* Vehicle registration + plate details
* Driver license class documentation (commercial)
* A copy of the client service agreement scope (recyclables pickup + reporting) and today’s route sheet/manifest

#### 3.2.2 Closing the remaining DLT classification uncertainty
We will obtain explicit written confirmation of how our model is classified by DLT and store it in `evidence/` (tracked as `CLAIM-DLT-YELLOW-001` in `evidence_register.json`). Until closed, we operate using the licensed partner bridge.

## 4. Facility & Processing
*   **Location:** **Phra Khanong Area (Pridi Soi 14 or similar)**.
*   **Function:** Consolidation, QC, Baling.
*   **Equipment:** Vertical Baler (Essential for selling PET/HDPE to processors). Baling increases density 10x, reducing transport cost to processors.
*   **Staffing (Month 12 Model):**
    *   1 Operations Manager.
    *   1 Driver.
    *   1 Loader (rides with driver).
    *   1 Sorter (facility based).

### 4.1 Fuel price logging (execution control)
Maintain a weekly diesel price log to support sensitivity analysis and trigger any surcharge clauses.

Cadence
- Every Friday by 12:00 local time.

Steps
1. Open `appendices/research_briefs/fuel/diesel_price_log.csv`.
2. Record: date (YYYY-MM-DD), station_name, district, price_thb_per_litre, source_url, captured_by.
3. Save the source (screenshot/PDF) in `appendices/research_briefs/fuel/` with the same date.
4. Notify finance if weekly average exceeds surcharge threshold.

QA
- Supervisor samples one entry per month; verify source file and accuracy.

## 5. Saleng Integration (The Hybrid Model)
*   **Partner:** Local aggregation hub near **Pridi Banomyong Soi 14**.
*   **Role:** We hire trusted local saleng as "Sub-contracted Sorters" or "Last-mile assist" for difficult-access lanes.
*   **Benefit:** Reduces friction with local informal sector; leverages their micro-logistics knowledge.
*   **Control:** Saleng must wear our vest/ID when on officially contracted sites.

### 5.1 Informal Collector Integration (anti-substitution strategy)
Purpose: Reduce substitution risk by integrating local collectors (saleng) ethically and audibly.

Models
- Subcontracted Micro-Buildings: Assign low-volume sites to trusted collectors; provider supplies signage and QA checks; pay per pickup.
- Buy-Back Guarantee: Provider guarantees purchase of clean, sorted fractions from collectors at posted rates; contamination deductions per spec.
- Hiring Pathway: Priority hiring for vetted collectors as loaders/drivers; training and PPE provided.

QA & Compliance
- Cleanliness specs by fraction (align with processor MOU template).
- Photo evidence on pickup; weigh estimates or spot-weighing.
- Incident escalation to operations with 24h resolution target.

Payment & Terms
- Weekly payments via transfer; deductions for contamination per posted table.
- Blackout for repeated non-compliance after warnings.

Onboarding
- Orientation on sorting standards and safety.
- Provide ID badge, QR for reporting issues, and contact sheet.

Risk Controls
- No hazardous waste handling.
- Background checks where feasible; supervisor ride-alongs initially.

Documentation
- Keep partner registry with contact details, service areas, and compliance history.

### 5.2 Processor offtake (quality + payment basics)
We standardize processor relationships using a simple MOU structure to reduce rejection risk and stabilize cash collection.

Materials and specifications (targets)
- PET (baled): moisture ≤ 5%, contamination ≤ 2%
- HDPE (baled): moisture ≤ 5%, contamination ≤ 3%
- OCC/Cardboard (baled): moisture ≤ 8%, contamination ≤ 3%
- Non-conforming loads may be downgraded or rejected with photo evidence.

Weighing and documentation
- Certified scale weight tickets at Buyer site.
- Chain-of-custody records: pickup time, vehicle plate, photos (pre/post), bale IDs.
- Discrepancies documented within 24 hours with photos.

Payment terms (target)
- Net 15 days from receipt of invoice and weigh tickets.
- Disputes raised within 5 business days; undisputed amounts payable on time.

## 6. Quality Assurance (QA)
*   **Contamination Loop:** If a building repeatedly fails (>15% contamination), we trigger a "Resident Education Event" (billed extra or part of contract).
*   **Missed Pickup:** If we miss a window, automatic 500 THB credit to client (Self-imposed SLA).
