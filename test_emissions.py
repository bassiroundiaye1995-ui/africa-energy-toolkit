import pytest
from aet.emissions import avoided_co2_kg

def test_avoided_co2():
    assert avoided_co2_kg(1000, 0.5) == pytest.approx(500)
