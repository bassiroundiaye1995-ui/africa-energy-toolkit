from dataclasses import dataclass

@dataclass(frozen=True)
class BatteryResult:
    nominal_kwh: float
    usable_kwh: float
    autonomy_days: float
    daily_energy_kwh: float
    depth_of_discharge: float
    round_trip_efficiency: float

def size_battery(
    daily_energy_kwh: float,
    autonomy_days: float = 1.0,
    depth_of_discharge: float = 0.80,
    round_trip_efficiency: float = 0.90,
) -> BatteryResult:
    """Estimate nominal battery capacity for a target autonomy period."""
    if daily_energy_kwh <= 0:
        raise ValueError("daily_energy_kwh must be greater than zero")
    if autonomy_days <= 0:
        raise ValueError("autonomy_days must be greater than zero")
    if not 0 < depth_of_discharge <= 1:
        raise ValueError("depth_of_discharge must be between 0 and 1")
    if not 0 < round_trip_efficiency <= 1:
        raise ValueError("round_trip_efficiency must be between 0 and 1")

    usable = daily_energy_kwh * autonomy_days
    nominal = usable / (depth_of_discharge * round_trip_efficiency)

    return BatteryResult(
        nominal_kwh=nominal,
        usable_kwh=usable,
        autonomy_days=autonomy_days,
        daily_energy_kwh=daily_energy_kwh,
        depth_of_discharge=depth_of_discharge,
        round_trip_efficiency=round_trip_efficiency,
    )
