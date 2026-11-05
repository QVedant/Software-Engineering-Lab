from hypothesis import given, strategies as st
from electricity_bill import units_consumed, daily_average, tariff_rate

@given(st.one_of(st.text(), st.none()))
def test_units_consumed_no_crash(s):
    units_consumed(s)

@given(st.one_of(st.text(), st.none()))
def test_daily_average_no_crash(s):
    daily_average(s)

@given(st.one_of(st.text(), st.none()))
def test_tariff_rate_no_crash(s):
    tariff_rate(s)
