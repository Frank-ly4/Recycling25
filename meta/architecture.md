## Architecture — modules and data flows

Modules
- Logistics: routing, pickup cadence, vehicle/fuel logs; KPIs: on_time_pickup_pct, bin_overflow_rate_pct, cost_per_ton_thb
- Materials: sorting, contamination control, inventory/baling; KPIs: diversion_rate_pct, contamination_pct, co2e_avoided_per_ton, cost_per_ton_thb
- Community: resident engagement, floor bins, incentives, NPS; KPIs: participation_rate_pct, nps
- Tech: data capture (weighing logs), reporting, PDPA compliance; KPIs: reporting cadence adherence
- Finance: pricing, invoicing, arrears protocol, sensitivity; KPIs: cost_per_ton_thb

Data flows
- Collection logs (by condo/date/material/weight) → Materials inventory → ESG monthly report → Finance invoicing
- Incident/overflow logs → Logistics review → SOP updates
- Engagement actions → Community tracking → Participation/NPS updates

KPI measurement points
- At intake scale (diversion, contamination)
- Route logs (on-time, overflow)
- Monthly reports (participation, CO2e, NPS)


