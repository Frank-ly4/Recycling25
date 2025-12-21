## KPI schema — Bangkok Zone A pilot

avg_total_kg_per_building_month
- Formula: total_recyclables_weight / active_buildings
- Source: intake scale logs + building IDs
- Cadence: monthly; Owner: Logistics Lead

avg_pet_kg_per_building_month
- Formula: pet_weight / active_buildings
- Source: intake scale logs (PET separated at intake or sorting)
- Cadence: monthly; Owner: Materials Lead

kg_per_unit_month
- Formula: total_recyclables_weight / total_units
- Source: intake scale logs; verified unit counts from juristic
- Cadence: monthly; Owner: Logistics Lead

diversion_rate_pct
- Formula: recycled_weight / eligible_recyclables_weight * 100
- Source: intake scale logs; baseline from waste audit or estimated composition
- Cadence: monthly; Owner: Materials Lead

contamination_pct
- Formula: contaminant_weight / intake_weight * 100 (spot-sample)
- Source: QC sampling logs at sorting tables
- Cadence: weekly; Owner: Materials Lead

cost_per_ton_thb
- Formula: (fuel+labor+facility+overhead attributable) / tons handled
- Source: finance records, route logs
- Cadence: monthly; Owner: Finance Lead

on_time_pickup_pct
- Formula: on-time pickups / scheduled pickups * 100
- Source: route schedule vs arrival scan logs
- Cadence: weekly; Owner: Logistics Lead

bin_overflow_rate_pct
- Formula: overflow events / bin checks * 100
- Source: arrival photos/logs
- Cadence: weekly; Owner: Logistics Lead

participation_rate_pct
- Formula: units contributing at least once / total units * 100
- Source: floor-bin counts, QR logs (if used), staff tallies
- Cadence: monthly; Owner: Community Lead

co2e_avoided_per_ton
- Formula: standard factors by material; report per ton handled
- Source: material mix; factor table (config)
- Cadence: monthly; Owner: Tech/Materials

nps
- Formula: %promoters - %detractors from manager survey (0–10)
- Source: quarterly survey to juristic managers
- Cadence: quarterly; Owner: Community Lead


