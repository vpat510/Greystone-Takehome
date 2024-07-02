# loan amortization calculator 
# term for paying down the cost of an asset at a certain rate 
# repaying the principle on a loan

# fully ammortizing loan -> down to 0 -> paid off
# https://www.youtube.com/watch?v=xKjsgMEXDV8

# EX: If you have a loan of $10,000 
# with an annual interest rate of 5% to be repaid over 12 months
# output = month, remaining balance (after that months payment), fixed monthly payment

# 1. convert annual interest rate to monthly interset rate
# r = 5 / (12 * 100) = 0.004167

# 2. calculate monthly payment
# M = 10,000 *  ( (0.004167 (1 + 0.004167)^12 ) / ( (1+0.004167)^12)-1 )
# M = 856.07

# First month: 
#   interest payment = 1000 * 0.004167 = 41.67
#   principal payment = 856.07 - 41.67 = 814.40
#   remaining balance = 1000 - 814.40 = 9185.60

# 2nd month:
#   interest payment = 9185.60 * 0.004167 = 38.27
#   Principal Payment = 856.07 − 38.27 = 817.80
#   Remaining Balance = 9185.60 − 817.80 = 8367.80

# keep going until remaining balance reaches 0

def calculate_amortization_schedule(amount, annual_interest_rate, loan_term_months):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    monthly_payment = amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months)

    schedule = []
    remaining_balance = amount

    for month in range(1, loan_term_months + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        schedule.append({
            "month": month,
            "remaining_balance": remaining_balance,
            "monthly_payment": monthly_payment
        })

    return schedule

def calculate_amortization_schedule(principal, annual_interest_rate, loan_term_months):
    # Convert annual interest rate to monthly interest rate (in decimal form)
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Calculate the fixed monthly payment using the amortization formula
    numerator = monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months
    denominator = (1 + monthly_interest_rate) ** loan_term_months - 1
    monthly_payment = principal * numerator / denominator

    # Initialize the amortization schedule list and remaining balance
    schedule = []
    remaining_balance = principal

    # Calculate the interest, principal, and remaining balance for each month
    for month in range(1, loan_term_months + 1):
        # Calculate the interest payment for the current month
        interest_payment = remaining_balance * monthly_interest_rate

        # Calculate the principal payment for the current month
        principal_payment = monthly_payment - interest_payment

        # Update the remaining balance
        remaining_balance -= principal_payment

        # Ensure the remaining balance does not become negative due to floating-point precision issues
        remaining_balance = max(remaining_balance, 0)

        # Append the current month's details to the schedule
        schedule.append({
            "month": month,
            "remaining_balance": remaining_balance,
            "monthly_payment": monthly_payment,
            "principal_payment": principal_payment,
            "interest_payment": interest_payment
        })

    return schedule



