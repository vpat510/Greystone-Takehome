from app.amortization import calculate_amortization_schedule

# Tests the calculate_amortization_schedule function to ensure it produces the correct schedule.
def test_calculate_amortization_schedule():
    amount = 10000
    annual_interest_rate = 5
    loan_term_months = 12
    schedule = calculate_amortization_schedule(amount, annual_interest_rate, loan_term_months)

    assert len(schedule) == 12
    assert schedule[0]["month"] == 1
    assert schedule[0]["monthly_payment"] > 0
    assert schedule[-1]["month"] == 12
    assert schedule[-1]["remaining_balance"] == 0