# Empty Promises Audit — Recycling25

Date: 2025-10-19

Scope: Identify promises, guarantees, outcomes, or offers lacking concrete how/when/resources; recommend fixes and structural supports.

## Executive summary
- Several marketing and contract phrases imply absolute outcomes or resourcing commitments without explicit backing. Most are easy to fix with qualified wording and supporting SOPs.
- "100%" completion claims in the legal documentation status conflict with widespread placeholders across the same documents; treat those files as templates pending customization and counsel review.

## Findings and recommended fixes

1) Marketing — assigned manager commitment
- Location: docs/GoToMarket/03_OnePager.md ("dedicated manager")
- Risk: Implies 1:1 resourcing regardless of scale.
- Fix: "assigned account manager (ratio ≤1:6 buildings), monthly review cadence." Add ratio to SLA Schedule D and modules/ops notes.

2) Crisis communications — unconditional liability language
- Locations: preservation/necessary_documentation/36_Crisis_Communication_Plan.md (core/key messages)
- Fix implemented: Qualified responsibility statements to tie to applicable law and contracts; added legal guardrails principle.

3) Contract — absolute sustainability outcome
- Location: preservation/necessary_documentation/11_Condo_Service_Agreement.md (Article 7.2 "Maximum diversion from landfill")
- Risk: Absolute outcome depends on resident behavior and Client cooperation.
- Fix: "Maximize diversion consistent with contamination thresholds and Client cooperation (Art. 4.3)."

4) Contract — time-bound operational promises without capacity proof
- Location: Condo agreement (backup collection ≤48h; equipment replacement ≤5 business days)
- Risk: Requires inventory, vendor SLAs, and routing reserve.
- Fix: Qualify as best efforts subject to access/Force Majeure/inventory; add Schedule C vendor/stock policy and escalation path.

5) ESG/CO2e reporting — placeholder factors
- Locations: docs/GoToMarket/07_ESG_Report_Template.md; config/co2e_factors.json (notes: illustrative factors)
- Risk: Over-claiming impact without cited Thai LCA.
- Fix: Add footnote in ESG template re: placeholder factors; load cited Thai/ASEAN LCA sources and version them in config.

6) Strategy phrasing — "Performance Guarantees"
- Location: preservation/COMPREHENSIVE_PROTECTION_STRATEGY.md
- Fix: Rephrase to "Performance credits per SLA if thresholds not met."

7) Pilot SLA — measurement clarity
- Location: docs/GoToMarket/05_Pilot_SLA.md (on-time ≥98%, overflow alerts ≤24h)
- Risk: Lacks operational measurement method.
- Fix: Reference SLA Measurement SOP (timestamps, definitions, alert workflow) and link in document footers.

## Document completion status — investigation
The file preservation/necessary_documentation/DOCUMENT_COMPLETION_STATUS.md claims multiple areas at "100%" completion. However, numerous legal documents contain placeholders such as [PENDING], [TO BE SPECIFIED], [Your Name], [TBD], etc. Examples:
- Crisis Plan: roles, contacts, vendors (e.g., [TO BE APPOINTED], [TO BE COMPLETED]).
- PDPA Policy: DPO, contacts, transfer arrangements ([TO BE SPECIFIED]).
- Condo Agreement: client identity, units, dates ([TO BE COMPLETED], [TO BE SPECIFIED]).
- Articles of Association, BMA Permit, Treaty of Amity, Investment Agreement: registration numbers, addresses, parties pending.

Conclusion: Treat these as comprehensive templates requiring customization and counsel review, not "100%" completed documents. Recommend revising the status language to "Templates prepared; customization and legal review required" and removing "100%" claims.

## AI-driven account management — outline (to back the promise)
- Objective: Deliver reliable "assigned account manager" experience using AI agents with human-in-the-loop.
- Agents/Pipelines:
  - SLA Monitor Agent: Watches pickup logs, timestamps, overflow events; flags SLA breaches; drafts customer updates.
  - Reporting Agent: Compiles monthly ESG using data store and CO2e factors; inserts footnotes and confidence notes.
  - Account Ops Agent: Schedules monthly reviews, summarizes issues/actions, drafts minutes and follow-ups.
  - Escalation Router: Routes incidents to human ops/legal; enforces PDPA redaction and approval gates.
- Guardrails: PDPA-compliant data handling; approval workflow for outbound emails; audit logs.
- KPIs: on-time %, response SLAs, NPS, ticket closure time, AM ratio ≤1:6.
- Next steps: Connect email/LINE, define data schema, configure triggers, add approval UI/macros, pilot on 1–2 buildings.

## Structural supports to close promises
- SLA Measurement SOP: Define on-time metric, data capture, audit trail, escalation, backup routing, and comms timelines.
- Equipment Inventory & Vendors SOP/Schedule C: Min stock levels, vendor SLAs, lead times, swap procedures.
- Processor documentation workflow: Certificates of proper disposal capture and surfacing in monthly reports.
- ESG methodology note: Factors provenance, revision cadence, participation/contamination assumptions.

## Change log
- 2025-10-19: Added audit; updated crisis plan liability phrasing; proposed fixes and AI AM outline.


