import pytest
from electricity_bill import energy_charge, late_fee, subsidy

# Example test cases:
def test_low_usage_domestic():
    assert energy_charge(50, "domestic") == 200

def test_paid_on_time():
    assert late_fee(500, 0) == 0

# --- energy_charge tests ---
def test_energy_charge_unknown_connection():
    # Tests the unknown connection ValueError branch
    with pytest.raises(ValueError, match="unknown connection"):
        energy_charge(50, "industrial")

def test_energy_charge_negative_units():
    # Tests the invalid units ValueError branch
    with pytest.raises(ValueError, match="invalid units"):
        energy_charge(-10, "domestic")

def test_energy_charge_mid_usage():
    # Tests the 101-300 unit slab
    assert energy_charge(200, "domestic") == 850

def test_energy_charge_high_usage_commercial():
    # Tests the >300 unit slab and commercial multiplier
    assert energy_charge(400, "commercial") == 4350

def test_energy_charge_exact_boundaries():
    # Tests exactly 100 and 300 unit boundaries
    assert energy_charge(100, "domestic") == 350
    assert energy_charge(300, "commercial") == 2750

# --- late_fee tests ---
def test_late_fee_within_15_days():
    # Tests the 1-15 days branch
    assert late_fee(500, 10) == 50

def test_late_fee_over_15_days_low_bill():
    # Tests >15 days but bill <= 2000
    assert late_fee(1000, 20) == 100

def test_late_fee_over_15_days_high_bill():
    # Tests >15 days and bill > 2000 (triggers additional penalty)
    assert late_fee(2100, 20) == 205

# --- subsidy tests ---
def test_subsidy_senior_low_usage_no_solar():
    # Tests senior discount without solar
    assert subsidy(100, True, False) == 50

def test_subsidy_not_senior_low_usage_solar():
    # Tests solar discount without senior discount
    assert subsidy(100, False, True) == 100

def test_subsidy_senior_high_usage_solar():
    # Tests solar benefit cancellation (units > 300)
    assert subsidy(400, True, True) == 0

def test_subsidy_mid_usage_solar():
    # Tests standard solar benefit (units between 101 and 300)
    assert subsidy(200, False, True) == 100

def test_subsidy_senior_low_usage_solar():
    # Tests combined senior and solar benefits
    assert subsidy(50, True, True) == 150