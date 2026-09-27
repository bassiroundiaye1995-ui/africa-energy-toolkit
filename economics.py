def annual_energy_cost(annual_consumption_kwh: float, tariff_per_kwh: float) -> float:
    """Calculate annual electricity cost from consumption and tariff."""
    if annual_consumption_kwh < 0:
        raise ValueError("annual_consumption_kwh cannot be negative")
    if tariff_per_kwh < 0:
        raise ValueError("tariff_per_kwh cannot be negative")
    return annual_consumption_kwh * tariff_per_kwh

def simple_payback_years(investment: float, annual_savings: float) -> float:
    """Calculate simple payback period in years."""
    if investment < 0:
        raise ValueError("investment cannot be negative")
    if annual_savings <= 0:
        raise ValueError("annual_savings must be greater than zero")
    return investment / annual_savings
