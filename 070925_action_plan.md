# Action Plan — Dependency-Based Task Flow

Source of truth: `070925assessment` (Sections 1–9). This plan removes deadlines and expresses a clear dependency flow. Tasks list prerequisites and produced artifacts so execution can proceed without strict chronology.

## 0) Impact vs Effort (for prioritizing what to pull first)

| Item | Impact | Effort | Note |
|---|---|---|---|
| Pricing guardrails + pilot SLA/KPIs | High | Low | Prevents underpricing; sets ops targets |
| Micro-cluster focus + prospect list | High | Low | Route density; quick wins |
| Vehicle access surveys (3–5 sites) | High | Low | De-risks fleet and pilot feasibility |
| Processor MOUs + price sheets | Medium | Low | Anchors materials revenue |
| Facility quotes (150–300 m²) | Medium | Low | Validates opex and lead times |
| BMA permit path/timeline | High | Medium | Critical path for operations |
| PDPA-lite framework | Medium | Low | Enables compliant data/reporting |
| Unit economics sensitivity table | High | Medium | Aligns pricing and risk |
| DIW trigger plan | High | Medium | Avoids scale stall |

## 1) Task Graph (dependencies only, not chronological)

- G1 Micro-cluster selection → F3 Prospect list
- M1 Unit-economics sensitivity table → F1 Pricing guardrails
- F3 Prospect list → F4 Outreach templates → F5 Manager interviews & LOIs → P1 Pilot agreements (3–5)
- L1 Company registration → L2 BMA permit application → P4 Pilot execution
- O1 Vehicle access surveys (3–5 buildings) → O2 Vehicle quotes → P2 Vehicle/equipment procurement → P3 Hire & train → P4 Pilot execution
- O5 Collection SOPs & training materials → P3 Hire & train → P4 Pilot execution
- O4 PDPA-lite framework → P1 Pilot agreements; P4 Pilot execution
- O3 Processor MOUs (≥2) → P2 Procurement; P4 Pilot execution
- S1 DIW trigger/structure memo → S4 Scale to 8–10 buildings
- S2 Case studies → S3 Investor materials → S4 Scale to 8–10 buildings

## 2) Task Catalog (single-owner, dependency-based)

Fields: ID, Description, Prerequisites, Produces, Priority (H/M/L), Success Metric, Blocks.

| ID | Description | Prerequisites | Produces | Priority | Success Metric | Blocks |
|---|---|---|---|---|---|---|
| G1 | Select single micro-cluster (adjacent neighborhoods) | — | Micro-cluster note | H | Named zone with map | F3 |
| M1 | Build unit-economics sensitivity table (price x units x undercut) | — | Sensitivity table | H | Table complete; ranges validated | F1, S3 |
| F1 | Define pricing guardrails (min/target/ceiling; inclusions/exclusions) | M1 | Pricing 1-pager | H | Approved guardrails | P1 |
| F2 | Draft pilot SLA & KPIs (miss rate, response time, credits) | — | SLA/KPI sheet | H | KPIs + credit rules | P1, P4 |
| F3 | Create prospect list (50–80 condos in G1) | G1 | Prospect CSV | H | ≥50 qualified leads | F4, O1 |
| F4 | Outreach templates (TH/EN) + LOI | F3 | Email + call scripts; LOI | H | Templates ready | F5 |
| F5 | Manager interviews (15–20) & LOIs (≥5) | F4 | Interview notes; LOIs | H | ≥5 LOIs or equivalent | P1, O1 |
| L1 | Register Thai-majority Ltd | — | Company docs; bank acct | H | Reg complete | L2 |
| L2 | Apply for BMA “Business Detrimental to Health” permit | L1 | Application receipt | H | Timeline confirmed | P4 |
| O1 | Vehicle access surveys (3–5 buildings) | F5 | Survey reports (photos/measures) | H | Constraints documented | O2, O5 |
| O2 | Vehicle quotes (N-series/FRR + financing) | O1 | Quotes & options | M | 2+ quotes | P2 |
| O3 | Processor MOUs (PET/HDPE/paper) + price sheets | — | 2+ signed MOUs | M | Floors in writing | P2, P4 |
| O4 | PDPA-lite framework (policy, consent, data capture) | — | PDPA docs | M | Policy + forms ready | P1, P4 |
| O5 | Collection SOPs & training materials | O1 | SOP pack | M | SOPs documented | P3, P4 |
| P1 | Convert LOIs to pilot agreements (3–5 buildings) | F1, F2, F5, O4 | Signed pilots | H | ≥3 signed | P2, P4 |
| P2 | Procure vehicle & equipment | O2, O3, P1 | Vehicle/equip on hand | H | Delivered + insured | P3 |
| P3 | Hire & train (driver, loader) | P2, O5 | Staff ready | H | Hires trained/certified | P4 |
| P4 | Execute 60–90 day pilot | L2, P3, O3, O4 | Pilot ops & data | H | KPIs met; CSAT >80% | S2, S4 |
| S1 | DIW trigger/structure memo | — | Trigger memo | H | Thresholds + actions | S4 |
| S2 | Case studies (≥3) | P4 | 3+ case studies | M | Published | S3 |
| S3 | Investor materials (deck, model, data room) | S2, M1 | Fundraising kit | M | Ready to pitch | S4 |
| S4 | Scale to 8–10 buildings | P4, S1, S3 | Operating plan | M | ≥8 live contracts | — |

Notes:
- Dependencies express gating logic; tasks without dependencies can be pulled early by Impact/Effort.
- Keep materials revenue ≤20% in planning (per `070925assessment`).
- Default fleet baseline: N-series unless O1 proves FRR feasible.

## 3) Evidence Gap Closure (fastest solo methods)

| ID | Evidence Need | Method | Output |
|---|---|---|---|
| E1 | ICP count (300–600 unit buildings) | Google Maps + registries tally | Count table |
| E2 | Competitor price bands | 10 calls + 3 manager interviews | Price bands memo |
| E3 | Dock/ramp constraints | O1 surveys with photos/measures | Survey pack |
| E4 | Route model (km/day, dwell) | GMaps spreadsheet | Route sheet |
| E5 | Tonnage per stream | 2 processor calls + public studies | Estimate table |
| E6 | Processor prices/specs | O3 MOUs + sheets | MOUs |
| E7 | Facility rent quotes | 3 broker calls | Quote summary |
| E8 | Labor comp ranges | Job boards + 2 recruiter calls | Benchmarks memo |
| E9 | Insurance/PDPA costs | Broker call + PDPA draft | Quote + policy |
| E10 | Permit timelines | District office call | Timeline memo |

## 4) Branch Decisions (guardrails)

- Pricing: Per-unit primary; test lump-sum with guardrails; postpone rev-share.
- Geography: Single micro-cluster first; postpone multi-district.
- Fleet: N-series baseline pending O1; postpone FRR unless access allows.
- Facility: 150–200 m² now; add baler at throughput threshold.
- Materials reliance: Cap planning ≤20%; diversify buyers; floors in MOUs.
- Tech: Off-the-shelf for routing/data; postpone custom build.
- Legal incentives: SE now (if applicable); BOI post-pilot.
- Scale: Postpone 15–20 until 8–10 stable.

## 5) Execution Notes

- Source documents: `070925assessment` is canonical. Update this plan after each milestone.
- Logging: Save substantive outputs to disk (not just chat). Use `meta/change_log/` for summaries.
- Versioning: Label updates `YYMMDDassessment_v{n}` and diff against `070925assessment`.


