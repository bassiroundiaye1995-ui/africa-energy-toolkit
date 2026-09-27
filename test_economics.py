import pytest
from aet.economics import annual_energy_cost, simple_payback_years

def test_annual_cost():
    assert annual_energy_cost(1000, 0.20) == pytest.approx(200)

def test_payback():
    assert simple_payback_years(10000, 2500) == pytest.approx(4)
