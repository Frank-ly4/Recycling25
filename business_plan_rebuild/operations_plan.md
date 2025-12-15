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

## 5. Saleng Integration (The Hybrid Model)
*   **Partner:** Local aggregation hub near **Pridi Banomyong Soi 14**.
*   **Role:** We hire trusted local saleng as "Sub-contracted Sorters" or "Last-mile assist" for difficult-access lanes.
*   **Benefit:** Reduces friction with local informal sector; leverages their micro-logistics knowledge.
*   **Control:** Saleng must wear our vest/ID when on officially contracted sites.

## 6. Quality Assurance (QA)
*   **Contamination Loop:** If a building repeatedly fails (>15% contamination), we trigger a "Resident Education Event" (billed extra or part of contract).
*   **Missed Pickup:** If we miss a window, automatic 500 THB credit to client (Self-imposed SLA).
