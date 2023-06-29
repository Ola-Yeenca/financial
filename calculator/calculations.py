import math
import decimal

# Compound interest calculations
# Compound interest calculation
def compound_interest(principal, rate, time):
    if principal is None or rate is None or time is None:
        return None
    amount = principal * decimal.Decimal(math.pow(1 + rate/100, time))
    ci = amount - principal
    return ci


# Loan payment calculation
def loan_payment(principal, rate, time):
    r = rate / 100 / 12  # monthly interest rate
    n = time * 12  # number of monthly payments
    payment = principal * r * math.pow(1 + r, n) / (math.pow(1 + r, n) - 1)
    return payment

# Investment return calculation
def investment_return(principal, rate, time):
    amount = principal * math.pow(1 + rate/100, time)
    return amount - principal

# Present value calculation
# Present value calculation
def present_value_input(future_value, rate, time):
    if future_value is None or rate is None or time is None:
        return None
    pv = future_value / math.pow(1 + rate/100, time)
    return pv


# Future value calculation
# Future value calculation
def future_value(present_value, rate, time):
    if present_value is None or rate is None or time is None:
        return None
    fv = present_value * decimal.Decimal(math.pow(1 + rate/100, time))
    return fv
