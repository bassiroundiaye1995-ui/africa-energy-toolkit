from aet.solar_pv import size_system
from aet.battery import size_battery

daily_load = 12
sun_hours = 5.5

pv = size_system(daily_load, sun_hours, system_efficiency=0.80)
battery = size_battery(daily_load, autonomy_days=1)

print(f"PV: {pv.required_kwp:.2f} kWp")
print(f"Battery: {battery.nominal_kwh:.2f} kWh")
