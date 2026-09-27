import pytest
from aet.battery import size_battery

def test_battery_sizing():
    result = size_battery(10, autonomy_days=1, depth_of_discharge=0.8, round_trip_efficiency=0.9)
    assert result.nominal_kwh == pytest.approx(13.8888889)

def test_invalid_dod():
    with pytest.raises(ValueError):
        size_battery(10, depth_of_discharge=0)
