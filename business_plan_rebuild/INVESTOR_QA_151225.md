# Investor Q&A (151225)

**Scope:** Answers are based on `business_plan_rebuild/` artifacts. Items requiring validation or benchmarks are explicitly tagged.

## Market Opportunity

### MO-01

**Question:** What is the total addressable market (TAM) for plastic bottle collection from condominiums in Bangkok, and how is it segmented by building type, size, and location?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: The internal pack currently provides a **Zone A SOM** sizing and an ICP definition rather than a fully evidenced Bangkok-wide TAM segmentation. Zone A pilot districts total ~122,000 units across ~300 large condos (>300 units), implying ~11.0M THB/month addressable service-fee opportunity at the modeled fee levels (see `market_analysis.md`).
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: A sizing methodology brief has been added (`appendices/research_briefs/market/20251215_TAM_Sizing_Methodology.md`). Close by acquiring a primary dataset (REIC/BMA equivalent), archiving it in `evidence/market/`, and rebuilding the Bangkok-wide TAM by district + size tiers.

### MO-02

**Question:** What is the estimated volume of PET bottles generated per condominium per month, and how does this vary across different districts or building demographics?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: The pack defines **measurement KPIs** (e.g., target >200 kg/building/month) and a pilot data collection plan, but does not yet contain a verified per-condo PET bottle generation distribution by district/demographics. We will measure actual weights per building during the pilot and use that to parameterize district-level variance.
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: Capture actual weights per building and contamination rates during pilot; add a district-level volume distribution once measured.

### MO-03

**Question:** How many condominiums are there in Bangkok, and what percentage have existing recycling programs or contracts with competitors?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: Internal pack contains two sizing anchors: (1) Zone A pilot districts (~300 large condos >300 units), and (2) pitch-deck headline estimate of **1,500+ large condos (>300 units) in Bangkok**. The percentage with existing recycling contracts/programs is not evidenced internally yet.
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: Validate condo counts and competitor penetration via REIC/market mapping; add evidence + competitor program scan.

### MO-04

**Question:** What are the current collection and recycling rates for plastic bottles in Bangkok’s residential sector, and how do these compare to national averages?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Benchmark sources have been added to the data room. A city-level benchmark from the Circulate Initiative report estimates that **~15% (≈134 kt/year) of plastic waste in Bangkok is recycled**, with the informal sector playing a dominant role (see `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, p.16). For a national benchmark, the US-ASEAN report states Thailand generates **~2 million metric tons of plastic waste annually** and **~25% is recycled** (see `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, p.30).
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: These are benchmarks (not our operational results). Add pilot-measured building-level capture rates to show our achievable uplift vs baseline.

### MO-05

**Question:** What are the key drivers of growth in the Bangkok plastic bottle recycling market (e.g., regulatory changes, consumer awareness, government incentives)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: The pack’s stated growth drivers are **BMA fee incentives for separation** and **developer ESG/HQ reporting mandates**, positioned as a compliance + reporting service rather than a commodity trader (see `market_analysis.md`, `executive_summary.md`, `outreach_kit/ESG_sales_talking_points.md`).
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`

### MO-06

**Question:** How does the business plan to expand beyond condominiums (e.g., to office buildings, hotels, schools), and what is the potential market size for these segments?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: Current execution plan is condominium-first (cluster density). Expansion beyond condos is mentioned as a roadmap concept, but the pack does not yet provide a quantified market size for offices/hotels/schools.
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: Add adjacent-segment sizing (office/hotel/school) as benchmarks; validate via 10–20 customer interviews + pilot conversion.

### MO-07

**Question:** What are the main barriers to entry for new players in the Bangkok plastic bottle collection market?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Barriers highlighted in the pack include regulatory compliance (BMA permit / DLT classification), operational constraints (truck bans, basement clearance), and the need for ESG-grade chain-of-custody reporting that informal collectors cannot provide (see `legal_compliance.md`, `operations_plan.md`, `market_analysis.md`).
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`

### MO-08

**Question:** How is the market expected to evolve over the next 5–10 years in terms of volume, pricing, and regulatory requirements?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Benchmark context has been added: Bangkok baseline recycling rate and supply-chain constraints (Circulate report) and Thailand national plastic waste baseline (US-ASEAN report). Regulatory trend benchmark: ERIA summarizes Thailand’s EPR progression under the Action Plan on Plastic Waste Management Phase II (2023–2027), including framework development and pilots before expected enactment (see `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`). A short internal outlook memo has been added to organize additional sources and implications (see `appendices/research_briefs/market/20251215_Thailand_Plastics_Outlook_Memo.md`).
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: Add a short forecast memo (volume/pricing) with 2–3 additional sources (e.g., resin/PET pricing indices, recycled content commitments) and summarize implications for our fee floor and offtake strategy.

### MO-09

**Question:** What is the impact of recent government initiatives (e.g., BMA’s “No Mixed Waste” program, waste separation fee incentives) on the market opportunity?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`

### MO-10

**Question:** How does the business plan to capture market share from informal collectors and established waste management companies?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Strategy is to **differentiate on compliance + reliability + reporting** and to reduce friction by **integrating** (not displacing) local saleng for last-mile support where appropriate (see `market_analysis.md`, `operations_plan.md`, `audits/INVESTOR_QA_CHECKLIST.md`).
- **Internal sources**: `market_analysis.md`, `executive_summary.md`, `outreach_kit/pitch_deck.md`, `audits/viability_check.md`, `evidence/bma/20251214_bma_greener_waste_fee_20_60.html`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`
- **Gaps / validation**: Quantified market-share capture plan (targets, pipeline) is not yet evidenced; tie to LOIs and pilot conversions.

## Business Model and Revenue Streams

### BM-01

**Question:** What is the core business model: direct collection and resale of bottles, provision of collection services to condominiums, or integrated recycling (collection plus processing)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Fee-for-service condo recycling program (bins + scheduled pickups + reporting) with optional upside from material sales; core profitability is modeled without relying on PET trading.
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

### BM-02

**Question:** What are the primary revenue streams (e.g., sale of PET bottles to recyclers, service fees from condominiums, carbon credits, data services)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Primary modeled revenue is contracted service fees (per unit / building fee). Material sales are treated as upside (kept at 0 in the base model for conservatism). We explicitly do **not** include carbon/plastic credit revenue in base projections; credits are treated as a staged option only (see `audits/impact_credits_positioning.md`).
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`, `audits/impact_credits_positioning.md`

### BM-03

**Question:** How are prices for collected PET bottles determined, and how volatile are these prices?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: The pack assumes a conservative PET price floor scenario and positions the business as **fees-first** to reduce sensitivity to PET price volatility (see `risk_register.md`, `audits/viability_check.md`, `executive_summary.md`).
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

### BM-04

**Question:** What is the typical contract structure with condominiums (e.g., exclusive agreements, revenue sharing, fixed service fees)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Canonical commercial structure is a B2B service agreement with a 12-month term (auto-renew), monthly invoicing (Net-15), SLA definitions/credits, and deposits for bins/signage (see `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`, `operations_plan.md`).
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

### BM-05

**Question:** Are there opportunities for value-added services (e.g., data analytics for ESG reporting, educational programs, branded recycling campaigns)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

### BM-06

**Question:** How does the business plan to monetize environmental impact (e.g., carbon credits, plastic credits, partnerships with brands seeking recycled content)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Near-term, we monetize impact indirectly through contracted service fees tied to compliance/reporting value. Carbon/plastic credits are **explicitly excluded** from base-case revenue and are only a staged option if a buyer/registry pathway is validated (see `audits/impact_credits_positioning.md`). 
- **Internal sources**: `investor_relations.md`, `audits/impact_credits_positioning.md`, `outreach_kit/ESG_sales_talking_points.md`

### BM-07

**Question:** What is the expected customer acquisition cost (CAC) for new condominium contracts, and what is the average contract duration?

- **Status**: `MISSING`
- **Answer**: Canonical commercial structure is a B2B service agreement with a 12-month term (auto-renew), monthly invoicing (Net-15), SLA definitions/credits, and deposits for bins/signage (see `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`, `operations_plan.md`).
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

### BM-08

**Question:** How does the business plan to retain customers and prevent churn, especially as competitors enter the market?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Retention strategy is service reliability (SLA), compliance reporting value (monthly ESG/diversion report), and operational hygiene (site survey + contamination controls) to reduce service failures (see `outreach_kit/ESG_sales_talking_points.md`, `operations_plan.md`, `outreach_kit/SLA_checklist.md`).
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

### BM-09

**Question:** What is the projected revenue mix over the next five years, and how does this align with market trends?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: The current financial model intentionally assumes **service-fee revenue only** (material revenue set to 0 in `financials/model_inputs.json`) to keep projections conservative; material sales are treated as upside in `audits/viability_check.md`.
- **Internal sources**: `executive_summary.md`, `outreach_kit/pitch_deck.md`, `outreach_kit/service_agreement_12m.md`, `investor_relations.md`

## Unit Economics and Financial Metrics

### UE-01

**Question:** What are the key unit economics for the business (e.g., cost per kilogram collected, revenue per kilogram, gross margin per collection route)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Core unit economics are modeled on a **per-unit service fee** basis (not per-kg commodity trading). Key drivers include service fee (90 THB/unit/month), variable cost (30 THB/unit/month), and clustered fixed-cost structure (see `financials/model_inputs.json`, `financials/model_spec.md`).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-02

**Question:** What are the main cost drivers (labor, transport, sorting, contamination management, storage, equipment depreciation)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Main cost drivers in the model are direct labor (driver/loader/sorter), fleet lease, facility rent, and fuel with step-ups as buildings increase (see `financials/model_inputs.json`, `financials/model_spec.md`).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-03

**Question:** What is the break-even volume per condominium or collection route?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Break-even is addressed via the generated model and sensitivity analysis (positive net income achieved at ~9 buildings in the base case; profit target ≥60k net income at ~12 buildings).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-04

**Question:** How does contamination (e.g., food waste in bottles) affect processing costs and material value?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Operationally, the pack sets contamination controls (e.g., >15% triggers rejection/penalty and education loop). Financially, the base model is conservative and does not rely on material margin; contamination primarily impacts the (optional) material upside (see `operations_plan.md`, `outreach_kit/SLA_checklist.md`).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-05

**Question:** What is the projected payback period for capital expenditures (e.g., vehicles, bins, sorting equipment)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Capex is framed via use-of-funds (fleet + facility/equipment + working capital) and investor repayment waterfall; the pack does not yet present a separate IRR/payback schedule for each asset class (see `investor_relations.md`, `financials/waterfall.json`).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-06

**Question:** How are fluctuations in PET prices and fuel costs modeled in financial projections?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Fuel sensitivity is explicitly tested in `financials/sensitivity_analysis.md` and the ops plan defines a weekly diesel logging control. PET price volatility is treated as non-core because repayment/profitability is modeled fees-first (see `risk_register.md`, `financials/sensitivity_analysis.md`).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-07

**Question:** What are the expected gross and net margins at scale, and how do these compare to industry benchmarks?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Unit economics and KPIs are modeled in `financials/*` (inputs → projections → cashflow → waterfall) and summarized in `sensitivity_analysis.md` and `metrics_dashboard.md`.
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-08

**Question:** What is the cash conversion cycle (from collection to sale and payment)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Cash timing policy is documented in `financials/model_spec.md` (model assumes Net-30; execution targets advance billing + Net-15). WHT reduces cash receipts (3% withheld) per `legal_compliance.md` and Revenue Department evidence files.
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-09

**Question:** How are bad debts, payment delays, or contract disputes accounted for in financial planning?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Payment-delay risk and mitigations are documented in `risk_register.md` and `investor_relations.md` (Net-15 terms, deposits, late fees, and a minimum cash buffer covenant for quarterly revenue-share).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

### UE-10

**Question:** What are the key financial KPIs tracked by management (e.g., EBITDA, ROIC, customer lifetime value)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: The pack’s financial KPIs are defined in `metrics_dashboard.md` (MRR, gross margin, cash runway; ops KPIs include on-time rate, weight/building, contamination).
- **Internal sources**: `financials/model_inputs.json`, `financials/model_spec.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`, `financials/sensitivity_analysis.md`, `metrics_dashboard.md`

## Competitive Landscape

### CL-01

**Question:** Who are the main competitors in the Bangkok plastic bottle collection and recycling market (e.g., informal collectors, established recycling firms, tech-enabled startups)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-02

**Question:** What are the market shares of key players, and how are they differentiated (e.g., technology, scale, customer relationships)?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance). A draft competitor landscape brief has been added to structure benchmarking and list what evidence must be archived to become investor-grade (see `appendices/research_briefs/market/20251215_Competitor_Landscape.md`).
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`
- **Gaps / validation**: Market share/player-level benchmarking is not yet evidenced and may require external benchmarking.

### CL-03

**Question:** How does the business plan to compete with the informal sector, which often operates at lower cost and with deep community ties?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-04

**Question:** What are the strengths and weaknesses of major competitors (e.g., Indorama Ventures, Wongpanit, EcoBlue, Wastebuy Delivery, Glean, Trash Lucky)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-05

**Question:** Are there any recent market entrants with disruptive technologies or business models (e.g., smart bins, blockchain tracking, gamified recycling)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-06

**Question:** What are the barriers to entry for new competitors, and how defensible is the business’s position?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-07

**Question:** How does the business plan to build and sustain competitive advantages (e.g., proprietary technology, exclusive contracts, brand partnerships)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-08

**Question:** What lessons can be learned from failed or struggling recycling startups in Thailand or similar markets?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

### CL-09

**Question:** How does the business monitor competitor activity and adapt its strategy accordingly?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Internal pack describes competitor categories (informal saleng, platform players, traditional haulers) and our differentiation (SLA + compliance reporting + insurance) in `market_analysis.md` and `audits/INVESTOR_QA_CHECKLIST.md`.
- **Internal sources**: `market_analysis.md`, `outreach_kit/pitch_deck.md`, `audits/INVESTOR_QA_CHECKLIST.md`

## Regulatory Environment and Permits

### RE-01

**Question:** What licenses and permits are required to operate a recycling business in Bangkok, and what is the status of each application (e.g., operating license, environmental permits, labor permits)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-02

**Question:** What are the requirements for machine power and employee numbers that trigger additional licensing (e.g., >50 HP, >50 employees)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-03

**Question:** How does the business ensure compliance with the National Environmental Quality Act, Public Health Act, and local BMA waste management regulations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-04

**Question:** What are the implications of the Foreign Business Act for ownership and control, and what structures (e.g., BOI promotion, preferential shares, FBL) are in place to ensure compliance?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-05

**Question:** What is the process and timeline for obtaining and renewing key permits, and what are the associated costs?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-06

**Question:** Are there any zoning or land use restrictions affecting the location of sorting or processing facilities?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-07

**Question:** How does the business ensure compliance with waste transport and storage regulations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-08

**Question:** What are the penalties for non-compliance, and how are regulatory risks monitored and managed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-09

**Question:** How does the business stay abreast of evolving regulations, such as the upcoming Extended Producer Responsibility (EPR) laws and the BMA’s new waste separation fee structure?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

### RE-10

**Question:** Are there any pending legal or regulatory actions against the company or its founders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Permits/licensing approach is defined in `legal_compliance.md` (BMA ‘business detrimental to health’ permit; DLT classification + license-bridge leasing strategy; VAT/WHT handling).
- **Internal sources**: `legal_compliance.md`, `evidence/`, `evidence_register.json`

## Board of Investment (BOI) Incentives and Foreign Ownership

### BOI-01

**Question:** Has the business applied for or received BOI promotion, and what incentives have been granted (e.g., tax holidays, 100% foreign ownership, land ownership rights)?

- **Status**: `MISSING`
- **Answer**: The internal pack does not yet state that the company has applied for or received BOI promotion. Current default structure is a Thai limited company with 51% Thai ownership (see `legal_compliance.md`).
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: Decision required: BOI pathway vs Thai-majority structure; if BOI pursued, document application status, activity category, incentives granted, and compliance obligations with archived evidence.

### BOI-02

**Question:** What is the minimum capital investment required for BOI eligibility, and how does the business meet this threshold?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Benchmark: BOI’s Investment Promotion Guide 2023 states a **minimum capital investment requirement of 1,000,000 THB per project (excluding land and working capital), unless otherwise specified** (see `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, p.9).
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: Confirm the specific minimum/conditions for the exact promoted activity category chosen (recycling / sorting / waste treatment) and location-based measures.

### BOI-03

**Question:** What are the reporting and compliance obligations under BOI promotion, and how are these managed?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Benchmark: BOI promotion includes ongoing reporting and compliance requirements; details vary by activity and incentives granted. Use the BOI guide as the starting reference and confirm obligations for the chosen activity category (see `evidence/boi/20251215_boi_a_guide_2023_en.pdf`).
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: Add a BOI compliance checklist (reporting cadence, permitted activities, audit readiness) once the BOI pathway decision is made.

### BOI-04

**Question:** How does BOI status affect the company’s ability to hire foreign staff and obtain work permits?

- **Status**: `MISSING`
- **Answer**: Benchmark: BOI promotion commonly provides non-tax privileges related to visas/work permits for foreign experts, subject to BOI conditions and the promoted activity category (see `evidence/boi/20251215_boi_a_guide_2023_en.pdf`).
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: Confirm headcount/skill requirements and the exact privilege set for the chosen BOI activity.

### BOI-05

**Question:** Are there any risks of BOI status being revoked or challenged, and what contingencies are in place?

- **Status**: `MISSING`
- **Answer**: Benchmark: BOI privileges can be revoked if conditions are not met (activity scope, reporting, investment realization, etc.).
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: If BOI pursued, add a risk memo describing revocation triggers and operational controls to stay compliant.

### BOI-06

**Question:** How does BOI promotion affect the business’s competitive position relative to non-BOI competitors?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Benchmark: BOI can improve competitiveness through tax/non-tax incentives (e.g., tax holidays, facilitation of foreign hiring), but compliance burden increases.
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: Model BOI vs non-BOI economics (tax savings vs compliance/admin costs) and decide before fundraising.

### BOI-07

**Question:** What is the process for renewing or expanding BOI incentives as the business grows?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Benchmark: BOI incentives/privileges may be expanded or amended with BOI approval as projects scale; process depends on activity and changes requested.
- **Internal sources**: `legal_compliance.md`, `evidence/boi/20251215_boi_a_guide_2023_en.pdf`, `evidence/boi/20251215_SEARCH_LOG.md`
- **Gaps / validation**: If BOI pursued, document the amendment/expansion pathway and trigger milestones (new facility, equipment, capacity).

## Operational Logistics and Collection Process

### OP-01

**Question:** What is the end-to-end process for collecting, sorting, and transporting plastic bottles from condominiums to recycling facilities?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-02

**Question:** How are collection routes optimized for efficiency and cost-effectiveness?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-03

**Question:** What equipment and vehicles are used, and what is the maintenance and replacement schedule?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-04

**Question:** How is contamination managed at the point of collection, and what training is provided to residents and staff?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-05

**Question:** What is the process for weighing, recording, and tracking collected materials?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-06

**Question:** How are storage and transfer stations managed to prevent theft, contamination, or regulatory violations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-07

**Question:** What are the key operational bottlenecks, and how are they addressed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-08

**Question:** How does the business ensure health and safety for workers, especially in high-density urban environments?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-09

**Question:** What contingency plans are in place for equipment failure, labor shortages, or supply chain disruptions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

### OP-10

**Question:** How is technology (e.g., smart bins, mobile apps, data analytics) integrated into operational workflows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: End-to-end collection SOP, route constraints (truck ban windows), mixed fleet strategy, contamination thresholds, and SLA measurement are defined in `operations_plan.md` and related audit/risk docs.
- **Internal sources**: `operations_plan.md`, `risk_register.md`, `audits/red_team_gap_analysis.md`, `outreach_kit/pilot_SLA.md`

## Supply Chain and Offtake Agreements

### SC-01

**Question:** Who are the primary buyers of collected PET bottles (e.g., local recyclers, export markets, brand partners), and what are the terms of offtake agreements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-02

**Question:** Are there long-term contracts in place with recyclers or processors, and what are the pricing mechanisms?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-03

**Question:** How is quality (e.g., contamination, color sorting) ensured to meet buyer specifications?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-04

**Question:** What is the process for negotiating and renewing offtake agreements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-05

**Question:** Are there risks of buyer concentration or dependency, and how are these mitigated?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-06

**Question:** How does the business monitor market prices and adjust sales strategies accordingly?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-07

**Question:** Are there opportunities for direct integration with processors or brand owners seeking recycled content?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-08

**Question:** What is the process for handling rejected or downgraded materials?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

### SC-09

**Question:** How does the business ensure traceability and transparency in the supply chain, especially for ESG reporting?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/_archive_reference_only/ops_playbooks/processor_mou_template.md`

## Technology and Processing Methods

### TP-01

**Question:** What technologies are used for sorting, cleaning, and processing collected bottles (e.g., manual sorting, mechanical separation, AI-powered smart bins)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-02

**Question:** Are there proprietary or patented technologies in use, and what are their advantages?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-03

**Question:** How is contamination detected and managed at each stage of processing?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-04

**Question:** What is the capacity and utilization rate of processing equipment, and how scalable is the system?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-05

**Question:** How does the business monitor and optimize energy and water usage in processing?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-06

**Question:** Are there plans to invest in advanced recycling technologies (e.g., chemical recycling, blockchain tracking)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-07

**Question:** How does the business stay abreast of technological innovations in the recycling sector?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-08

**Question:** What are the maintenance and upgrade requirements for key equipment?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

### TP-09

**Question:** How is technology used to track and report environmental impact (e.g., carbon footprint, plastic credits)?

- **Status**: `MISSING`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### TP-10

**Question:** Are there partnerships with technology providers or research institutions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pitch_deck.md`, `metrics_dashboard.md`

## Team and Founders Background

### TF-01

**Question:** Who are the founders and key management team members, and what are their backgrounds in recycling, logistics, technology, or business development?

- **Status**: `MISSING`
- **Answer**: The pack now includes a dedicated team snapshot file, but the bios are still placeholders pending founder-provided details. See `team_bios.md` and the pitch deck Team slide.
- **Internal sources**: `team_bios.md`, `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Replace TBD placeholders with named bios (4–8 bullets each) and add links/CVs under `evidence/` if appropriate.

### TF-02

**Question:** What is the track record of the team in launching and scaling similar ventures?

- **Status**: `MISSING`
- **Answer**: Track record will be captured in `team_bios.md` once founder bios are provided (prior ventures, relevant wins, and execution proof).
- **Internal sources**: `team_bios.md`, `governance.md`
- **Gaps / validation**: Fill the “Relevant wins” section per founder and add references (public links or evidence attachments).

### TF-03

**Question:** How is the team structured, and what are the roles and responsibilities of each member?

- **Status**: `MISSING`
- **Answer**: Team structure and responsibilities will be codified in `team_bios.md` (roles + KPI ownership) and aligned with governance approvals in `governance.md`.
- **Internal sources**: `team_bios.md`, `governance.md`
- **Gaps / validation**: Add a simple RACI table (Founder/Sales/Ops/Finance/Compliance) for investor clarity.

### TF-04

**Question:** What is the company’s approach to recruiting, training, and retaining talent at all levels?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

### TF-05

**Question:** Are there any gaps in the team’s expertise, and how are these being addressed?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

### TF-06

**Question:** What is the composition and experience of the board of directors and advisory board?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

### TF-07

**Question:** Are there any conflicts of interest or related-party transactions involving the founders or key staff?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

### TF-08

**Question:** What is the company culture, and how is it aligned with the mission and operational demands of the business?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

### TF-09

**Question:** How does the team engage with stakeholders (e.g., residents, local authorities, partners)?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

### TF-10

**Question:** What succession planning is in place for key roles?

- **Status**: `MISSING`
- **Answer**: Team bios/track record and governance specifics are not yet fully detailed in the pack (pitch deck only lists role archetypes).
- **Internal sources**: `outreach_kit/pitch_deck.md`, `governance.md`
- **Gaps / validation**: Add founder bios, roles/RACI, advisory board, conflicts disclosures, and vesting details; include evidence (CVs/refs) in data room.

## Labor, Informal Sector, and Community Integration

### LI-01

**Question:** How does the business interact with the informal sector (e.g., saleng, waste pickers), and what is the impact on collection volumes and community relations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-02

**Question:** Are there partnerships or agreements with informal collectors, and how are these structured?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-03

**Question:** What is the company’s policy on fair wages, working conditions, and social protection for workers?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-04

**Question:** How does the business address potential conflicts or competition with informal collectors?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-05

**Question:** Are there community engagement programs to build trust and encourage participation in recycling?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-06

**Question:** How does the business measure and report on social impact (e.g., job creation, income improvement for informal workers)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-07

**Question:** What is the approach to integrating marginalized or vulnerable groups into the workforce?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-08

**Question:** How does the business handle labor disputes, turnover, or shortages?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-09

**Question:** Are there partnerships with NGOs, local associations, or government agencies to support labor integration?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

### LI-10

**Question:** What is the company’s approach to health and safety, especially for workers handling potentially hazardous materials?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `appendices/research_briefs/wages/20251024_Wage_Benchmarks.md`

## Environmental Impact and Measurement

### EI-01

**Question:** What is the estimated environmental impact of the business (e.g., tons of plastic diverted from landfill, CO2 emissions avoided)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-02

**Question:** How is environmental performance measured, tracked, and reported (e.g., life cycle assessment, carbon footprint analysis)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-03

**Question:** What certifications or standards does the business adhere to (e.g., ISO 15270:2008, carbon credit schemes)?

- **Status**: `MISSING`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### EI-04

**Question:** How does the business ensure proper handling and disposal of non-recyclable or contaminated materials?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-05

**Question:** Are there initiatives to reduce the environmental footprint of operations (e.g., fuel-efficient vehicles, renewable energy, water recycling)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-06

**Question:** How does the business communicate environmental impact to customers, partners, and regulators?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-07

**Question:** Are there partnerships with academic or research institutions to validate impact claims?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-08

**Question:** How does the business plan to scale its environmental impact as it grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-09

**Question:** What are the risks of greenwashing, and how are these mitigated?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

### EI-10

**Question:** How does the business contribute to broader environmental goals (e.g., Thailand’s BCG strategy, zero plastic waste targets)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`

## Scalability and Expansion Plan

### SE-01

**Question:** What is the roadmap for scaling operations within Bangkok and to other cities or building types?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-02

**Question:** What are the key operational, regulatory, and financial milestones for expansion?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-03

**Question:** How does the business plan to replicate its model in new markets (e.g., standard operating procedures, technology transfer, local partnerships)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-04

**Question:** What are the main constraints to scaling (e.g., capital, labor, regulatory approvals, customer acquisition)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-05

**Question:** How does the business plan to manage quality and consistency as it grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-06

**Question:** What is the projected timeline for reaching key scale targets (e.g., number of buildings, tons collected, revenue milestones)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-07

**Question:** Are there plans for vertical integration (e.g., owning processing facilities, developing branded recycled products)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-08

**Question:** How does the business plan to adapt to changing market conditions or regulatory environments in new locations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-09

**Question:** What is the approach to managing risk and uncertainty during rapid growth?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

### SE-10

**Question:** How does the business benchmark its scalability against leading players in Thailand and the region?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `executive_summary.md`, `operations_plan.md`, `financials/model_inputs.json`

## Operational Risks and Contingency Planning

### OR-01

**Question:** What are the main operational risks facing the business (e.g., equipment failure, labor shortages, supply chain disruptions, regulatory changes)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-02

**Question:** What contingency plans are in place for each major risk?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-03

**Question:** How does the business monitor and respond to emerging risks (e.g., market downturns, commodity price shocks, pandemics)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-04

**Question:** What insurance coverage is in place for key assets, liabilities, and business interruptions?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### OR-05

**Question:** How does the business ensure business continuity in the event of natural disasters, political unrest, or other external shocks?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-06

**Question:** What is the process for incident reporting, investigation, and corrective action?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-07

**Question:** How are risks communicated to stakeholders, including investors, customers, and employees?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-08

**Question:** What is the company’s track record in managing past crises or disruptions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-09

**Question:** Are there regular risk assessments and scenario planning exercises?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

### OR-10

**Question:** How does the business balance risk mitigation with the need for innovation and growth?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `risk_register.md`, `operations_plan.md`, `governance.md`

## Financials, Projections, and Use of Funds

### FP-01

**Question:** What are the detailed financial projections for the next 3–5 years, including revenue, costs, margins, and cash flow?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-02

**Question:** What are the key assumptions underlying these projections, and how are they validated?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-03

**Question:** How will the $1–2 million investment be allocated (e.g., equipment, working capital, marketing, technology, hiring)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-04

**Question:** What is the expected runway provided by the investment, and what are the milestones for subsequent funding rounds?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-05

**Question:** How are capital expenditures prioritized and managed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-06

**Question:** What is the company’s approach to financial discipline and cost control?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-07

**Question:** Are there audited financial statements or third-party reviews of financial data?

- **Status**: `MISSING`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### FP-08

**Question:** What is the current burn rate, and how does this compare to industry benchmarks?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-09

**Question:** What are the main financial risks, and how are they mitigated?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

### FP-10

**Question:** How does the company plan to achieve profitability and positive cash flow, and on what timeline?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `financials/projections.json`, `financials/cashflow.json`, `financials/waterfall.json`

## Capital Requirements and Cap Table

### CC-01

**Question:** What is the current capitalization table, including all shareholders, option pools, and convertible instruments?

- **Status**: `MISSING`
- **Answer**: A cap table artifact has been added (`cap_table.md`), but it is still marked ASSUMPTION—VALIDATE pending the official shareholder register and confirmation of any options/convertibles.
- **Internal sources**: `cap_table.md`, `investor_relations.md`, `governance.md`
- **Gaps / validation**: Populate `cap_table.md` from the official shareholder register and explicitly list any SAFEs/notes/warrants/options (or state NONE).

### CC-02

**Question:** How will the new investment affect ownership structure and dilution for existing and new investors?

- **Status**: `MISSING`
- **Answer**: A dilution model template has been added (`dilution_model.md`) to show how an equity round would affect ownership; it cannot be finalized until `cap_table.md` is populated with actual shareholders and any instruments.
- **Internal sources**: `cap_table.md`, `dilution_model.md`, `equity_terms_summary.md`
- **Gaps / validation**: Fill pre-investment fully diluted ownership, then run 1–2 valuation scenarios to compute post-money dilution.

### CC-03

**Question:** What are the terms of the proposed investment (e.g., valuation, preferred shares, liquidation preferences, anti-dilution provisions)?

- **Status**: `MISSING`
- **Answer**: The pack now includes a draft equity terms outline (`equity_terms_summary.md`) as an alternative to the revenue-share structure described in `investor_relations.md`.
- **Internal sources**: `equity_terms_summary.md`, `investor_relations.md`, `governance.md`
- **Gaps / validation**: Replace TBDs with agreed terms and ensure narrative matches the selected structure.

### CC-04

**Question:** Are there any outstanding convertible notes, SAFEs, or warrants that could affect future dilution?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

### CC-05

**Question:** What is the company’s approach to managing dilution and aligning incentives for founders, employees, and investors?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

### CC-06

**Question:** How is the option pool structured, and what is the plan for future employee equity grants?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

### CC-07

**Question:** Are there any restrictions on foreign ownership or transfer of shares under Thai law or company bylaws?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

### CC-08

**Question:** How is the cap table managed and updated, and who has access to this information?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

### CC-09

**Question:** What are the exit rights and obligations for investors (e.g., drag-along, tag-along, ROFR)?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

### CC-10

**Question:** How does the cap table compare to industry norms for similar-stage startups?

- **Status**: `MISSING`
- **Answer**: Cap table and instrument-level dilution details are not yet present in the pack.
- **Internal sources**: `investor_relations.md`, `governance.md`
- **Gaps / validation**: Add cap table, option pool policy, and draft term sheet (or chosen structure).

## Exit Strategy and Liquidity Options

### EX-01

**Question:** What are the potential exit scenarios for investors (e.g., acquisition, IPO, secondary sale, founder buyback, liquidation)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-02

**Question:** What is the expected timeline for exit, and what milestones must be achieved to enable a successful exit?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-03

**Question:** Who are the likely acquirers or strategic partners (e.g., large recycling firms, FMCG brands, infrastructure funds)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-04

**Question:** What is the company’s track record or relationships with potential acquirers?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-05

**Question:** How does the business plan to maximize valuation at exit (e.g., scale, profitability, strategic partnerships)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-06

**Question:** What are the legal and tax implications of different exit scenarios for foreign investors?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-07

**Question:** Are there any restrictions on share transfers or exit under Thai law or company bylaws?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-08

**Question:** What is the process for preparing the company for exit (e.g., financial audits, legal due diligence, operational readiness)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-09

**Question:** How are exit rights structured in the investment agreement (e.g., drag-along, tag-along, put options)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

### EX-10

**Question:** What lessons can be learned from recent exits in the Thai recycling sector, and how does the company benchmark against these precedents?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`

## Legal Structure, Contracts, and Intellectual Property

### LC-01

**Question:** What is the legal structure of the company (e.g., Thai limited company, BOI-promoted entity, joint venture), and how does this affect ownership, control, and liability?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-02

**Question:** Are all key contracts (e.g., customer agreements, supplier contracts, employment agreements, leases) in place and legally enforceable?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-03

**Question:** What is the status of intellectual property (e.g., patents, trademarks, proprietary technology), and how is it protected?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-04

**Question:** Are there any pending or threatened legal disputes involving the company or its founders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-05

**Question:** How does the company ensure compliance with Thai contract law, labor law, and other relevant statutes?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-06

**Question:** Are there standard templates for key contracts, and how are these reviewed and updated?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-07

**Question:** How does the company manage confidentiality, data protection, and non-compete agreements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-08

**Question:** Are there any restrictions on foreign ownership or control under Thai law, and how are these addressed in the legal structure?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-09

**Question:** What is the process for resolving disputes with customers, suppliers, or employees?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

### LC-10

**Question:** How does the company ensure legal compliance as it expands into new markets or business lines?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `outreach_kit/service_agreement_12m.md`, `pdpa/PDPA_Compliance_Policy.md`

## Insurance, Liability, and Compliance

### IC-01

**Question:** What insurance coverage is in place for key risks (e.g., property, liability, business interruption, environmental liability)?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: The pack now includes an investor-facing insurance program summary (`insurance_program.md`). Final limits and bound policies remain ASSUMPTION—VALIDATE until broker quotes/policy schedules are archived.
- **Internal sources**: `insurance_program.md`, `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`
- **Gaps / validation**: Obtain broker quote(s) and archive policy schedules under `evidence/insurance/`; map coverage to risks in `risk_register.md`.

### IC-02

**Question:** How are insurance policies reviewed and updated as the business grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-03

**Question:** What are the main liability risks (e.g., worker injury, environmental contamination, contract disputes), and how are these managed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-04

**Question:** How does the company ensure compliance with health and safety regulations for workers and customers?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-05

**Question:** Are there regular audits or inspections to ensure compliance with insurance and regulatory requirements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-06

**Question:** What is the process for reporting and managing incidents or claims?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-07

**Question:** How does the company manage compliance with data protection and privacy laws, especially for customer and employee data?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-08

**Question:** Are there any recent or pending insurance claims or regulatory actions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-09

**Question:** How does the company benchmark its compliance practices against industry standards?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

### IC-10

**Question:** What is the process for updating compliance policies in response to regulatory changes?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `legal_compliance.md`, `operations_plan.md`, `outreach_kit/pilot_SLA.md`, `pdpa/PDPA_Compliance_Policy.md`

## Pricing, Incentives, and Customer Acquisition

### PC-01

**Question:** How are service fees and material prices set for condominium customers and recycling buyers?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-02

**Question:** What incentives are offered to residents, building managers, or staff to encourage participation in recycling programs?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-03

**Question:** How does the business acquire new condominium customers, and what is the typical sales cycle?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-04

**Question:** What marketing and outreach strategies are used to build brand awareness and trust?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-05

**Question:** How does the company measure and optimize customer acquisition cost (CAC) and lifetime value (LTV)?

- **Status**: `MISSING`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### PC-06

**Question:** Are there referral or loyalty programs to encourage customer retention and word-of-mouth growth?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-07

**Question:** How does the business adapt pricing and incentives in response to market changes or competitor actions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-08

**Question:** What is the process for onboarding new customers and ensuring high participation rates?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-09

**Question:** How are customer feedback and complaints managed and used to improve services?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

### PC-10

**Question:** What is the company’s track record in winning and retaining key accounts?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `investor_relations.md`, `outreach_kit/ESG_sales_talking_points.md`, `outreach_kit/service_agreement_12m.md`

## Partnerships with Local Authorities and LAOs

### PA-01

**Question:** What relationships exist with the Bangkok Metropolitan Administration (BMA), local administrative organizations (LAOs), and other government bodies?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-02

**Question:** Are there formal partnerships or MOUs in place, and what are their terms?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-03

**Question:** How does the business navigate the regulatory and political landscape at the local level?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-04

**Question:** What is the process for securing permits, approvals, or support from local authorities?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-05

**Question:** How does the company engage with community leaders, residents’ associations, and other stakeholders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-06

**Question:** Are there risks of policy changes, political shifts, or regulatory crackdowns affecting operations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-07

**Question:** How does the business contribute to local government goals (e.g., waste reduction targets, community development)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-08

**Question:** What is the process for resolving disputes or challenges with local authorities?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-09

**Question:** Are there opportunities for public-private partnerships or joint ventures with government agencies?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

### PA-10

**Question:** How does the business monitor and adapt to changes in local policy or leadership?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `legal_compliance.md`, `evidence/bma/`

## Quality Control and Contamination Management

### QC-01

**Question:** What processes are in place to ensure the quality and purity of collected materials?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-02

**Question:** How is contamination detected, tracked, and minimized at each stage of collection and processing?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-03

**Question:** What training is provided to staff and residents to reduce contamination?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-04

**Question:** How are contaminated or non-recyclable materials handled and disposed of?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-05

**Question:** What are the financial and operational impacts of contamination on margins and offtake agreements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-06

**Question:** How does the business benchmark its quality control processes against industry standards?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-07

**Question:** Are there regular audits or inspections of collection and processing sites?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-08

**Question:** How is feedback from buyers or processors used to improve quality?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-09

**Question:** What is the process for investigating and resolving quality issues?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

### QC-10

**Question:** How does the company plan to improve quality control as it scales?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `outreach_kit/pilot_SLA.md`

## Logistics: Transport, Storage, and Transfer Stations

### LG-01

**Question:** What is the fleet size and composition for collection and transport, and how is it managed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-02

**Question:** How are routes planned and optimized for efficiency and cost savings?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-03

**Question:** What storage facilities are used, and how are they secured and maintained?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-04

**Question:** How are transfer stations managed to prevent theft, contamination, or regulatory violations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-05

**Question:** What is the process for scaling logistics capacity as the business grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-06

**Question:** How are logistics costs tracked and controlled?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-07

**Question:** What is the company’s approach to fleet maintenance, replacement, and upgrade?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-08

**Question:** Are there partnerships with third-party logistics providers or local transport companies?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-09

**Question:** How does the business ensure compliance with transport and storage regulations?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

### LG-10

**Question:** What contingency plans are in place for logistics disruptions (e.g., vehicle breakdowns, road closures, labor strikes)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `audits/vehicle_specs_comparison.md`

## Market Trends and Forecasts for Thailand Plastics

### MT-01

**Question:** What are the key trends in plastic consumption, waste generation, and recycling rates in Thailand and Bangkok?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Benchmarks added: Thailand-scale plastic waste and recycling baseline from US-ASEAN report (see `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`) and Bangkok city supply-chain benchmark from Circulate (see `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`). Policy trend benchmark: Thailand EPR progress / timeline is summarized by ERIA (see `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`).
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-02

**Question:** How are government policies (e.g., plastic bag bans, EPR laws, BCG strategy) shaping the market?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Benchmarks added: Thailand-scale plastic waste and recycling baseline from US-ASEAN report (see `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`) and Bangkok city supply-chain benchmark from Circulate (see `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`). Policy trend benchmark: Thailand EPR progress / timeline is summarized by ERIA (see `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`).
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-03

**Question:** What is the outlook for PET prices, demand for recycled content, and export opportunities?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Benchmarks added: Thailand-scale plastic waste and recycling baseline from US-ASEAN report (see `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`) and Bangkok city supply-chain benchmark from Circulate (see `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`). Policy trend benchmark: Thailand EPR progress / timeline is summarized by ERIA (see `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`).
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-04

**Question:** How are consumer attitudes toward recycling and sustainability evolving?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-05

**Question:** What are the main risks and opportunities in the Thai plastics market over the next 5–10 years?

- **Status**: `BENCHMARK_EXTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### MT-06

**Question:** How does the business benchmark its forecasts against industry data and expert analysis?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-07

**Question:** What are the implications of global trends (e.g., plastic waste import bans, ESG investing) for the business?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Benchmarks added: Thailand-scale plastic waste and recycling baseline from US-ASEAN report (see `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`) and Bangkok city supply-chain benchmark from Circulate (see `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`). Policy trend benchmark: Thailand EPR progress / timeline is summarized by ERIA (see `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`).
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-08

**Question:** How does the company plan to adapt to changing market conditions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-09

**Question:** What is the process for monitoring and responding to market shifts?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

### MT-10

**Question:** How does the business leverage market trends to drive growth and innovation?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `market_analysis.md`, `appendices/research_briefs/`, `evidence/market/20251215_usasean_plastics_biannual_report_2023.pdf`, `evidence/market/20251215_circulate_th_selected_cities_plastic_recycling_supply_chains.pdf`, `evidence/policy/20251215_eria_thailand_epr_legal_framework.html`

## Customer Contracts and Condominium Agreements

### CA-01

**Question:** What is the standard contract structure with condominium customers (e.g., exclusivity, service levels, pricing, duration)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-02

**Question:** How are contracts negotiated, renewed, and enforced?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-03

**Question:** What are the main reasons for contract termination or non-renewal, and how are these addressed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-04

**Question:** How does the business ensure compliance with contract terms and service level agreements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-05

**Question:** Are there any disputes or legal actions involving customer contracts?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-06

**Question:** How does the company manage customer onboarding, training, and support?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-07

**Question:** What is the process for handling customer complaints or service issues?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-08

**Question:** How are contract terms adapted for different customer segments (e.g., luxury vs. budget condominiums)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-09

**Question:** What is the company’s track record in winning and retaining key accounts?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

### CA-10

**Question:** How does the business benchmark its contract terms against industry standards?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/service_agreement_12m.md`, `outreach_kit/pilot_SLA.md`

## Community Engagement and Behavior Change

### CE-01

**Question:** What programs are in place to educate and engage residents, building managers, and staff in recycling?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-02

**Question:** How does the business measure and report on participation rates and behavior change?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-03

**Question:** Are there partnerships with schools, NGOs, or community groups to promote recycling?

- **Status**: `ASSUMPTION_VALIDATE`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### CE-04

**Question:** What incentives or rewards are offered to encourage participation?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-05

**Question:** How does the company address cultural or behavioral barriers to recycling?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-06

**Question:** What is the process for gathering and acting on community feedback?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-07

**Question:** How are success stories and impact communicated to stakeholders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-08

**Question:** What is the company’s track record in driving sustained behavior change?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-09

**Question:** How does the business plan to scale community engagement as it grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

### CE-10

**Question:** What lessons have been learned from past engagement efforts, and how are these applied to future programs?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `outreach_kit/pilot_SLA.md`, `outreach_kit/ESG_sales_talking_points.md`

## Technology for Tracking and Reporting

### TR-01

**Question:** What systems are in place for tracking collection volumes, contamination rates, and operational performance?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-02

**Question:** How is data collected, stored, and analyzed, and who has access to it?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-03

**Question:** What reporting tools are used for internal management, customer communication, and regulatory compliance?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-04

**Question:** How does the business ensure data accuracy, security, and privacy?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-05

**Question:** Are there opportunities to monetize data (e.g., ESG reporting, plastic credits, customer dashboards)?

- **Status**: `MISSING`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### TR-06

**Question:** How is technology used to support decision-making and continuous improvement?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-07

**Question:** What is the process for integrating new technologies or upgrading existing systems?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-08

**Question:** Are there partnerships with technology providers or research institutions?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-09

**Question:** How does the company benchmark its technology stack against industry leaders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

### TR-10

**Question:** What is the plan for scaling technology infrastructure as the business grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `operations_plan.md`, `metrics_dashboard.md`, `pdpa/PDPA_Compliance_Policy.md`

## Capital Efficiency and Unit Scaling

### CU-01

**Question:** What is the capital required to launch and scale a new collection route or building?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-02

**Question:** How does the business optimize capital allocation for maximum impact and ROI?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-03

**Question:** What is the process for evaluating and prioritizing new investments (e.g., vehicles, equipment, technology)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-04

**Question:** How does the company benchmark its capital efficiency against industry norms?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-05

**Question:** What are the main constraints to scaling (e.g., capital, labor, regulatory approvals), and how are these addressed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-06

**Question:** What is the expected payback period for key investments?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-07

**Question:** How does the business plan to improve capital efficiency as it grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-08

**Question:** What is the process for monitoring and managing capital expenditures?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-09

**Question:** How are capital requirements modeled in financial projections?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

### CU-10

**Question:** What is the company’s track record in managing capital efficiently?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `financials/model_inputs.json`, `financials/sensitivity_analysis.md`, `audits/viability_check.md`

## Due Diligence on Suppliers and Equipment

### DS-01

**Question:** Who are the main suppliers of equipment, vehicles, and materials, and what are the terms of supply agreements?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-02

**Question:** How are suppliers selected, evaluated, and managed?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-03

**Question:** What is the process for vetting new suppliers or equipment vendors?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-04

**Question:** Are there risks of supply chain disruption, and how are these mitigated?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-05

**Question:** How does the company ensure quality, reliability, and compliance from suppliers?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-06

**Question:** What is the process for negotiating and renewing supply contracts?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-07

**Question:** Are there opportunities for strategic partnerships or joint ventures with suppliers?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-08

**Question:** How does the business benchmark supplier performance against industry standards?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-09

**Question:** What is the process for handling supplier disputes or failures?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

### DS-10

**Question:** How does the company plan to scale supplier relationships as it grows?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `audits/vehicle_specs_comparison.md`, `appendices/research_briefs/facility/20251024_Broker_Facility_Quotes_RFI.md`, `appendices/research_briefs/facility/20251025_Facility_Rent_Reality_Brief.md`

## Social Impact and ESG Metrics

### ESG-01

**Question:** What are the key social impact metrics tracked by the business (e.g., jobs created, income improvement for informal workers, community engagement)?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-02

**Question:** How is impact measured, validated, and reported to stakeholders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-03

**Question:** What certifications or standards does the business adhere to (e.g., B Corp, ISO, GRI)?

- **Status**: `MISSING`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`
- **Gaps / validation**: If this item requires quantified benchmarks or third-party validation, mark as a gap and close via pilot evidence / quotes / regulator confirmation.

### ESG-04

**Question:** How does the company align its operations with ESG (Environmental, Social, Governance) best practices?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-05

**Question:** Are there partnerships with NGOs, government agencies, or academic institutions to support impact measurement?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-06

**Question:** How does the business communicate impact to customers, partners, and investors?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-07

**Question:** What is the process for continuous improvement in social and environmental performance?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-08

**Question:** How are impact metrics integrated into management decision-making?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-09

**Question:** What is the company’s track record in delivering and scaling social impact?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`

### ESG-10

**Question:** How does the business benchmark its impact against industry leaders?

- **Status**: `SOURCED_INTERNAL`
- **Answer**: Covered (or partially covered) in the internal data room; see the referenced internal sources for the current position.
- **Internal sources**: `metrics_dashboard.md`, `operations_plan.md`, `governance.md`
