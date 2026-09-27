def avoided_co2_kg(
    annual_clean_energy_kwh: float,
    grid_emission_factor_kg_per_kwh: float,
) -> float:
    """Estimate avoided CO2 emissions from displaced grid electricity."""
    if annual_clean_energy_kwh < 0:
        raise ValueError("annual_clean_energy_kwh cannot be negative")
    if grid_emission_factor_kg_per_kwh < 0:
        raise ValueError("grid_emission_factor_kg_per_kwh cannot be negative")
    return annual_clean_energy_kwh * grid_emission_factor_kg_per_kwh
