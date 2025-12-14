from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _get(d: Dict[str, Any], path: str) -> Any:
    cur: Any = d
    for part in path.split("."):
        cur = cur[part]
    return cur


@dataclass(frozen=True)
class ModelInputs:
    horizon_months: int
    buildings_by_month: List[int]
    units_per_building: int

    fee_per_unit: float
    material_revenue_per_month: float

    variable_cost_per_unit: float
    fuel_base: float
    fuel_step: float
    fuel_step_buildings: int

    facility_rent: float
    vehicle_lease_primary: float
    vehicle_rescue_budget: float

    salary_ops_manager: float
    salary_driver: float
    salary_loader: float
    salary_sorter: float
    sorter_start_month: int

    misc_contingency: float

    one_time_costs: List[Dict[str, Any]]

    corporate_tax_rate: float
    wht_rate: float
    collection_delay_months: int

    starting_cash: float

    investor_principal: float
    investor_revenue_share_pct: float
    investor_cap_multiple: float
    investor_payment_frequency_months: int
    investor_first_payment_month: int

    @property
    def investor_cap_amount(self) -> float:
        return self.investor_principal * self.investor_cap_multiple


def load_inputs(model_inputs_path: Path) -> Tuple[ModelInputs, str]:
    raw_bytes = model_inputs_path.read_bytes()
    raw = json.loads(raw_bytes.decode("utf-8"))
    sha = _sha256_bytes(raw_bytes)

    horizon = int(_get(raw, "meta.horizon_months"))
    buildings = list(_get(raw, "drivers.volume.buildings_by_month"))
    if len(buildings) != horizon:
        raise ValueError(f"buildings_by_month length {len(buildings)} != horizon_months {horizon}")

    inputs = ModelInputs(
        horizon_months=horizon,
        buildings_by_month=buildings,
        units_per_building=int(_get(raw, "drivers.volume.units_per_building.value")),
        fee_per_unit=float(_get(raw, "drivers.pricing.service_fee_per_unit.value")),
        material_revenue_per_month=float(_get(raw, "drivers.pricing.material_revenue_per_month.value")),
        variable_cost_per_unit=float(_get(raw, "drivers.variable_costs.variable_cost_per_unit.value")),
        fuel_base=float(_get(raw, "drivers.variable_costs.fuel.base.value")),
        fuel_step=float(_get(raw, "drivers.variable_costs.fuel.step_per_n_buildings.value")),
        fuel_step_buildings=int(_get(raw, "drivers.variable_costs.fuel.step_buildings.value")),
        facility_rent=float(_get(raw, "drivers.fixed_costs.facility_rent.value")),
        vehicle_lease_primary=float(_get(raw, "drivers.fixed_costs.vehicle_lease_primary.value")),
        vehicle_rescue_budget=float(_get(raw, "drivers.fixed_costs.vehicle_rescue_budget.value")),
        salary_ops_manager=float(_get(raw, "drivers.fixed_costs.salaries.ops_manager.value")),
        salary_driver=float(_get(raw, "drivers.fixed_costs.salaries.driver.value")),
        salary_loader=float(_get(raw, "drivers.fixed_costs.salaries.loader.value")),
        salary_sorter=float(_get(raw, "drivers.fixed_costs.salaries.sorter.value")),
        sorter_start_month=int(_get(raw, "drivers.fixed_costs.salaries.sorter_start_month.value")),
        misc_contingency=float(_get(raw, "drivers.fixed_costs.misc_contingency.value")),
        one_time_costs=list(_get(raw, "drivers.one_time_cash_costs")),
        corporate_tax_rate=float(_get(raw, "drivers.tax_and_cash_policy.corporate_tax_rate.value")),
        wht_rate=float(_get(raw, "drivers.tax_and_cash_policy.withholding_tax_rate.value")),
        collection_delay_months=int(_get(raw, "drivers.tax_and_cash_policy.cash_collection_delay_months.value")),
        starting_cash=float(_get(raw, "drivers.starting_cash.value")),
        investor_principal=float(_get(raw, "drivers.investor_waterfall.principal.value")),
        investor_revenue_share_pct=float(_get(raw, "drivers.investor_waterfall.revenue_share_pct.value")),
        investor_cap_multiple=float(_get(raw, "drivers.investor_waterfall.cap_multiple.value")),
        investor_payment_frequency_months=int(_get(raw, "drivers.investor_waterfall.payment_frequency_months.value")),
        investor_first_payment_month=int(_get(raw, "drivers.investor_waterfall.first_payment_month.value")),
    )

    return inputs, sha


def fuel_cost_for_buildings(inputs: ModelInputs, buildings: int) -> float:
    if buildings <= 0:
        return 0.0
    steps = (max(0, buildings - 1)) // inputs.fuel_step_buildings
    return inputs.fuel_base + inputs.fuel_step * steps


def direct_labor_for_month(inputs: ModelInputs, month: int) -> float:
    base = inputs.salary_driver + inputs.salary_loader
    if month >= inputs.sorter_start_month:
        base += inputs.salary_sorter
    return base


def one_time_costs_for_month(inputs: ModelInputs, month: int) -> List[Dict[str, Any]]:
    return [c for c in inputs.one_time_costs if int(c.get("month")) == month]


def generate(inputs: ModelInputs, input_sha: str) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
    generated_at = _utc_now_iso()

    projections_rows: List[Dict[str, Any]] = []
    cashflow_rows: List[Dict[str, Any]] = []
    waterfall_rows: List[Dict[str, Any]] = []

    # Precompute revenue series for investor repayment calculations.
    service_revenue_by_month: List[float] = []
    total_revenue_by_month: List[float] = []

    for month in range(1, inputs.horizon_months + 1):
        buildings = int(inputs.buildings_by_month[month - 1])
        units = buildings * inputs.units_per_building

        revenue_service = units * inputs.fee_per_unit
        revenue_material = inputs.material_revenue_per_month
        revenue_total = revenue_service + revenue_material

        var_cost = units * inputs.variable_cost_per_unit
        fuel_cost = fuel_cost_for_buildings(inputs, buildings)

        direct_labor = direct_labor_for_month(inputs, month)
        admin = inputs.salary_ops_manager

        fixed = (
            inputs.facility_rent
            + inputs.vehicle_lease_primary
            + inputs.vehicle_rescue_budget
            + inputs.misc_contingency
        )

        ebitda = revenue_total - var_cost - fuel_cost - direct_labor - admin - fixed
        tax = max(0.0, ebitda) * inputs.corporate_tax_rate
        net_income = ebitda - tax

        projections_rows.append(
            {
                "month": month,
                "buildings": buildings,
                "units": units,
                "revenue_service": round(revenue_service, 2),
                "revenue_material": round(revenue_material, 2),
                "revenue_total": round(revenue_total, 2),
                "cost_variable": round(var_cost, 2),
                "cost_fuel": round(fuel_cost, 2),
                "cost_direct_labor": round(direct_labor, 2),
                "cost_admin": round(admin, 2),
                "cost_fixed_other": round(fixed, 2),
                "ebitda": round(ebitda, 2),
                "tax_simplified": round(tax, 2),
                "net_income": round(net_income, 2),
            }
        )

        service_revenue_by_month.append(revenue_service)
        total_revenue_by_month.append(revenue_total)

    # Cashflow + waterfall
    cash_balance = inputs.starting_cash
    cumulative_paid = 0.0
    cap_amount = inputs.investor_cap_amount

    def is_payment_month(m: int) -> bool:
        if m < inputs.investor_first_payment_month:
            return False
        return (m - inputs.investor_first_payment_month) % inputs.investor_payment_frequency_months == 0

    for month in range(1, inputs.horizon_months + 1):
        # Cash in: delayed collections of service revenue (excluding VAT), net of WHT
        collect_month = month - inputs.collection_delay_months
        cash_in_gross = service_revenue_by_month[collect_month - 1] if collect_month >= 1 else 0.0
        wht_withheld = cash_in_gross * inputs.wht_rate
        cash_in_net = cash_in_gross - wht_withheld

        # Cash out: treat costs as paid in-month
        proj = projections_rows[month - 1]
        cash_out_operating = (
            proj["cost_variable"]
            + proj["cost_fuel"]
            + proj["cost_direct_labor"]
            + proj["cost_admin"]
            + proj["cost_fixed_other"]
        )

        otc = one_time_costs_for_month(inputs, month)
        cash_out_one_time = sum(float(c["value"]) for c in otc) if otc else 0.0

        investor_payment = 0.0
        if is_payment_month(month) and cumulative_paid < cap_amount:
            q_start = month - inputs.investor_payment_frequency_months + 1
            q_start = max(1, q_start)
            q_revenue = sum(service_revenue_by_month[q_start - 1 : month])
            planned = q_revenue * inputs.investor_revenue_share_pct
            remaining = cap_amount - cumulative_paid
            investor_payment = min(planned, remaining)
            cumulative_paid += investor_payment
            waterfall_rows.append(
                {
                    "payment_month": month,
                    "quarter_start_month": q_start,
                    "quarter_end_month": month,
                    "quarter_service_revenue": round(q_revenue, 2),
                    "revenue_share_pct": inputs.investor_revenue_share_pct,
                    "payment_amount": round(investor_payment, 2),
                    "cumulative_paid": round(cumulative_paid, 2),
                    "cap_amount": round(cap_amount, 2),
                    "cap_remaining": round(cap_amount - cumulative_paid, 2),
                }
            )

        cash_out_total = cash_out_operating + cash_out_one_time + investor_payment

        cash_start = cash_balance
        cash_balance = cash_balance + cash_in_net - cash_out_total

        ar_end = service_revenue_by_month[month - 1]  # Net-30 simplification: AR equals current month service revenue

        cashflow_rows.append(
            {
                "month": month,
                "cash_start": round(cash_start, 2),
                "cash_in_service_gross": round(cash_in_gross, 2),
                "wht_withheld": round(wht_withheld, 2),
                "cash_in_service_net": round(cash_in_net, 2),
                "cash_out_operating": round(cash_out_operating, 2),
                "cash_out_one_time": round(cash_out_one_time, 2),
                "cash_out_investor": round(investor_payment, 2),
                "cash_end": round(cash_balance, 2),
                "accounts_receivable_end": round(ar_end, 2),
            }
        )

    projections = {
        "meta": {
            "generated_at": generated_at,
            "input_file": "model_inputs.json",
            "input_sha256": input_sha,
            "currency": "THB",
        },
        "rows": projections_rows,
    }

    cashflow = {
        "meta": {
            "generated_at": generated_at,
            "input_file": "model_inputs.json",
            "input_sha256": input_sha,
            "starting_cash": inputs.starting_cash,
        },
        "rows": cashflow_rows,
    }

    waterfall = {
        "meta": {
            "generated_at": generated_at,
            "input_file": "model_inputs.json",
            "input_sha256": input_sha,
            "principal": inputs.investor_principal,
            "cap_multiple": inputs.investor_cap_multiple,
            "cap_amount": round(inputs.investor_cap_amount, 2),
            "revenue_share_pct": inputs.investor_revenue_share_pct,
            "payment_frequency_months": inputs.investor_payment_frequency_months,
        },
        "rows": waterfall_rows,
        "totals": {
            "cumulative_paid": round(sum(r["payment_amount"] for r in waterfall_rows), 2),
            "cap_amount": round(inputs.investor_cap_amount, 2),
            "cap_remaining": round(inputs.investor_cap_amount - sum(r["payment_amount"] for r in waterfall_rows), 2),
        },
    }

    return projections, cashflow, waterfall


def main() -> None:
    here = Path(__file__).resolve().parent
    inputs_path = here / "model_inputs.json"
    projections_path = here / "projections.json"
    cashflow_path = here / "cashflow.json"
    waterfall_path = here / "waterfall.json"

    inputs, sha = load_inputs(inputs_path)
    projections, cashflow, waterfall = generate(inputs, sha)

    _write_json(projections_path, projections)
    _write_json(cashflow_path, cashflow)
    _write_json(waterfall_path, waterfall)

    print("Generated:")
    print(f"- {projections_path}")
    print(f"- {cashflow_path}")
    print(f"- {waterfall_path}")


if __name__ == "__main__":
    main()


