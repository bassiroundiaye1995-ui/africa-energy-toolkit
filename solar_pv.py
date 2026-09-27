from dataclasses import dataclass

@dataclass(frozen=True)
class PVResult:
    required_kwp: float
    daily_energy_kwh: float
    peak_sun_hours: float
    system_efficiency: float

def size_system(
    daily_energy_kwh: float,
    peak_sun_hours: float,
    system_efficiency: float = 0.80,
) -> PVResult:
    """Estimate PV capacity needed to meet a daily energy target.

    Formula:
        PV kWp = daily energy / (peak sun hours × system efficiency)

    This is a first-pass sizing calculation, not a detailed PV design.
    """
    if daily_energy_kwh <= 0:
        raise ValueError("daily_energy_kwh must be greater than zero")
    if peak_sun_hours <= 0:
        raise ValueError("peak_sun_hours must be greater than zero")
    if not 0 < system_efficiency <= 1:
        raise ValueError("system_efficiency must be between 0 and 1")

    required_kwp = daily_energy_kwh / (peak_sun_hours * system_efficiency)

    return PVResult(
        required_kwp=required_kwp,
        daily_energy_kwh=daily_energy_kwh,
        peak_sun_hours=peak_sun_hours,
        system_efficiency=system_efficiency,
    )
