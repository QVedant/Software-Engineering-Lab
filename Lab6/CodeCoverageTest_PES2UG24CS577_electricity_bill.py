import pytest
from electricity_bill import energy_charge, late_fee, subsidy

# Example test cases:
def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200

def test_paid_on_time():
    assert late_fee(500, 0) == 0

# Minimum tests to hit every line of code (Line Coverage)
def test_energy_charge_errors():
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")

def test_energy_charge_slabs():
    assert energy_charge(200, "domestic") == 850
    assert energy_charge(400, "commercial") == 4350

def test_late_fee_penalties():
    assert late_fee(500, 10) == 50
    assert late_fee(2500, 20) == 225

def test_subsidy_benefits():
    assert subsidy(50, True, False) == 50
    assert subsidy(400, False, True) == 0