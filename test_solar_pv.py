import pytest
from aet.solar_pv import size_system

def test_pv_sizing():
    result = size_system(12, 5.5, 0.80)
    assert result.required_kwp == pytest.approx(2.7272727)

def test_invalid_energy():
    with pytest.raises(ValueError):
        size_system(0, 5)

def test_invalid_efficiency():
    with pytest.raises(ValueError):
        size_system(10, 5, 1.2)
