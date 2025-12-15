# Financial Assumptions - Bangkok Condo Recycling Service

## Core Assumptions

### Revenue Assumptions
- **Base pricing**: 90 THB per unit per month (Standard Tier 50%)
- **Price increases**: 5% annual increase in Years 2-3
- **Collection rate**: 100% (building-level billing, not individual unit billing)
- **Units per building**: Average 400 units per building
- **Buildings**: Starting with 1 building (Month 1), scaling to 14 buildings by Month 36
- **Material sales revenue**: Excluded from model (conservative approach)

### Cost Assumptions

#### Variable Costs
- **Collection costs**: 30 THB per unit per month (33% of base price)
  - Includes: Fuel (6 THB), Bags/consumables (4 THB), Labor allocation (18 THB), Maintenance (2 THB)
  - Source: Fuel costs are based on a bottom-up calculation of ~11,253 THB/month for a fully utilized vehicle (see `research/evidence/fuel/20251025_Fuel_Route_Reality_Brief.md`), which aligns with the 6 THB/unit variable cost allocation.
  - Source: Labor costs based on Bangkok minimum wage plus 30% for benefits

#### Fixed Costs
- **Base monthly OPEX**: 50,000 THB (Months 1-5)
  - Facility rent: 25,000 THB (150 m² @ ~167 THB/m² - Source: research/evidence/facility/20251025_Facility_Rent_Reality_Brief.md)
  - Management salary: 15,000 THB (part-time initially)
  - Insurance & admin: 10,000 THB (Est. annual insurance ~45,000 THB, leaving ~6,250 THB/month for other admin. Source: research/evidence/vehicle_insurance/20251025_Vehicle_Insurance_Reality_Brief.md)
  - Source: Bangkok warehouse rental rates from Plus Property Market Report 2024

- **Scaling OPEX**:
  - 53,000 THB (Months 6-8): Additional part-time sorter
  - 57,000 THB (Months 9-12): Increased insurance and admin costs
  - 65,000 THB (Months 13-18): Full-time management
  - 73,000 THB (Months 19-24): Additional sorter
  - 85,000 THB (Months 25-30): Larger facility (200 m²)
  - 92,000 THB (Months 31-36): Additional admin support
  - Source: Bangkok labor rates from Thailand Department of Labor Protection and Welfare

### Capital Expenditure (Not in P&L)
- **Vehicle**: 800,000 THB (Isuzu N-series or equivalent. Note: This is a realistic minimum; all-in cost with customizations may be ~850,000 THB. Source: research/evidence/vehicle_insurance/20251025_Vehicle_Insurance_Reality_Brief.md)
  - Depreciation period: 5 years (not included in monthly P&L)
- **Bins and equipment**: 10,000 THB per building
  - Depreciation period: 3 years (not included in monthly P&L)
- **Initial facility setup**: 100,000 THB
  - Depreciation period: 3 years (not included in monthly P&L)

## Growth Assumptions

### Customer Acquisition
- Month 1: 1 building (400 units)
- Month 2: 2 buildings (800 units)
- Month 3: 3 buildings (1,200 units)
- Month 4: 4 buildings (1,600 units)
- Month 5-8: 5 buildings (2,000 units)
- Month 9-12: 6 buildings (2,400 units)
- Month 13-15: 7 buildings (2,800 units)
- Month 16-18: 8 buildings (3,200 units)
- Month 19-21: 9 buildings (3,600 units)
- Month 22-24: 10 buildings (4,000 units)
- Month 25-27: 11 buildings (4,400 units)
- Month 28-30: 12 buildings (4,800 units)
- Month 31-33: 13 buildings (5,200 units)
- Month 34-36: 14 buildings (5,600 units)

### Churn Assumptions
- 0% churn in Year 1 (12-month contracts)
- 5% annual churn in Years 2-3 (replaced with new buildings in acquisition targets)

## Sensitivity Analysis

### Critical Variables
1. **Price per unit**: Base case 90 THB
   - Downside: 80 THB (-11%)
   - Upside: 100 THB (+11%)
   - Impact: ±11% on revenue, ±16% on net profit

2. **Variable cost per unit**: Base case 30 THB
   - Downside: 35 THB (+17%)
   - Upside: 25 THB (-17%)
   - Impact: ±17% on variable costs, ±25% on net profit

3. **Fixed OPEX**: Base case as outlined
   - Downside: +15% on all fixed costs
   - Upside: -10% on all fixed costs
   - Impact: ±15%/-10% on fixed costs, ±13%/-9% on net profit

4. **Building acquisition rate**: Base case as outlined
   - Downside: 1 month delay in all new building additions
   - Upside: 1 month acceleration in all new building additions
   - Impact: ±8% on annual revenue, ±12% on annual net profit

5. **Material Sales Revenue (Upside Case)**: Based on market prices (see `research/evidence/processors/20251025_Processor_Prices_Reality_Brief.md`), each building could generate an additional 5,000-9,000 THB/month in revenue. This is excluded from the primary forecast but can act as a buffer or accelerator for profitability.

### Break-Even Analysis
- **Units required for break-even**: ~560 units (Month 2)
- **Buildings required for break-even**: 2 buildings (assuming 400 units/building)
- **Months to profitability**: 2 months
- **Months to 50,000 THB profit**: 5 months

### Profit Targets
- **50,000 THB monthly profit**: Achieved in Month 5
- **100,000 THB monthly profit**: Achieved in Month 9
- **200,000 THB monthly profit**: Achieved in Month 22
- **300,000 THB monthly profit**: Achieved in Month 34

## Funding Requirements
- **Initial capital**: 1,200,000 THB
  - Vehicle: 800,000 THB
  - Initial bins and equipment: 50,000 THB
  - Facility setup: 100,000 THB
  - Working capital: 250,000 THB (covers first 2 months of negative cash flow)

- **Tranche-based funding**:
  - Tranche 1: 1,200,000 THB (pre-launch)
  - Tranche 2: 800,000 THB (Month 6, contingent on 5+ buildings signed)
  - Total funding: 2,000,000 THB

## Sources
1. Fuel costs: Thailand Department of Energy Business, Average Diesel Price Bangkok, July 2025
2. Labor costs: Thailand Department of Labor Protection and Welfare, Minimum Wage Guidelines, 2025
3. Warehouse rental: Plus Property Market Report, Bangkok Industrial Space Q2 2024
4. Vehicle costs: Isuzu Thailand Commercial Vehicle Price List, 2025
5. Operational benchmarks: Waste Management Association of Thailand, Industry Metrics Report, 2024
