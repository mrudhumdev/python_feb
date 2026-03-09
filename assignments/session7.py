# Session – 7

# Task 1: The Secure Vault Gateway
# Analogy: A vault requires a primary key and an optional secondary biometric override.
# Requirement: Define a function access_vault with one mandatory positional argument
# user_id and two keyword-only arguments (using the * separator): pincode and
# biometric_id (defaulting to None).
# Technical Goal: Master the use of Keyword-Only Arguments to prevent accidental
# credential leaking through positional placement.

def access_vault(user_id,*,pincode,biometric_id=None):
    if pincode == "1234" or biometric_id == "VALID_BIO":
        return f"Access granted for {user_id}"
    return "Access denied"

print(access_vault("user1", pincode="1234"))

print(access_vault("user1", pincode="222"))


# Task 2: The Bulk Transfer Processor
# Analogy: A corporate client wants to send different amounts to various subsidiaries in
# one go.
# Requirement: Define a function execute_bulk_transfer that accepts a
# sender_account (positional) and a variable number of amounts using *args.
# Side Effect vs. Return: The function must print a ledger line for every transfer (side
# effect) but return the final remaining balance after subtracting all amounts from a
# starting balance of 10,000.

def execute_bulk_transfer(sender_account, *args):
    balance = 10000

    for args in args:
        print(f"Ledger: {sender_account} -> transfer {args}")
        balance -= args

    return balance


execute_bulk_transfer("sender1",500,200,100)


# Task 3: Dynamic Fee Policy
# Analogy: Different countries have different tax/fee keys.
# Requirement: Define a function calculate_net_amount that uses **kwargs to accept
# various tax rates (e.g., vat=0.15, service_fee=0.05).
# Logic: The function should take a base_amount and iterate through the kwargs to apply
# all taxes dynamically, returning the final figure.

def calculate_net_amount(base_amount, **kwargs):
    total = base_amount

    for fee_name, rate in kwargs.items():
        tax_amount = base_amount * rate
        total += tax_amount

    return total

print(calculate_net_amount(1000, vat=0.15, service_fee=0.05))

# Task 4: The Currency Arbitrage Scanner
# Analogy: A trader needs to know the Buy price, Sell price, and the Spread (difference)
# simultaneously.
# Requirement: Create a function get_market_rates(ticker). It must return a Tuple
# containing three floats: (buy_price, sell_price, spread).
# Technical Goal: Demonstrate Multiple Return Values and show how the caller can use
# "Under-score ignoring" (e.g., buy, _, spread = get_market_rates('USD')) if they
# don't need the sell price.

def get_market_rates(ticker):
    buy_price = 100.0
    sell_price = 102.5
    spread = sell_price - buy_price

    return buy_price, sell_price, spread

buy, sell, spread = get_market_rates("USD")
print(buy, sell, spread)

buy, _, spread = get_market_rates("EUR")
print(buy, spread)

# Task 5: Account Validation Wrapper
# Analogy: Before a transaction, a system checks if the account is active and if the KYC
# (Know Your Customer) is complete.
# Requirement: Write a function validate_account_status(account_id).
# Return Logic: It must return a Nested Tuple: (status_code, (is_active,
# kyc_complete)).
# Challenge: The candidate must write a calling script that uses Nested Unpacking to
# extract kyc_complete in a single line.

def validate_account_status(account_id):
    status_code = 200
    is_active = True
    kyc_complete = False

    return (status_code, (is_active, kyc_complete))

status_code, (is_active, kyc_complete) = validate_account_status("ACC1")

print(status_code)
print(is_active)
print(kyc_complete)


# Task 6: The Auditor’s Google-Style Docstring
# Analogy: Regulators require every financial calculation to be perfectly documented for
# audits.
# Requirement: Take a complex function that calculates Compound Interest. Write a
# complete Google-Style Docstring.
# Criteria: Must include Args:, Returns:, and a Yields: section (if applicable) or
# Raises: section for ValueError on negative interest rates.

def calculate_compound_interest(principal, rate, time, compounds_per_year=1):

    if rate < 0:
        print("Interest rate cannot be negative")
    else:
        amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
        return amount

print(calculate_compound_interest(1000, 0.05, 2))

print(calculate_compound_interest(1000, 0.1, 3))
    

# Task 7: NumPy-Style Scientific Schema
# Analogy: The Risk Assessment team uses NumPy-style documentation for their
# mathematical models.
# Requirement: Define a function calculate_risk_score(data_points,
# sensitivity). Write the docstring using NumPy formatting (using underlines for
# sections). Ensure types like array-like or float are correctly specified.

def calculate_risk_score(data_points, sensitivity):

    average = sum(data_points) / len(data_points)
    return average * sensitivity

print(calculate_risk_score([1, 2, 3], 1.5))
print(calculate_risk_score([10, 20, 30], 0.8))
print(calculate_risk_score([5, 5, 5], 2))



# Task 8: The "Print vs. Return" Audit
# Requirement: Provide a code snippet where a function uses print() inside its body to
# show a result, but forgets the return statement.
# Task: The candidate must debug why the variable result = my_function() evaluates
# to None and explain the architectural danger of using print as a substitute for data flow
# in a production pipeline.

def addition():
    add=1+5
    print(add)

addition() 

# or else we can define inside the function and give value as well
def my_function(a,b):
    sub=a-b
    return sub

print(my_function(3,1))
# If we return inside the function we need to print the values ouside it
# or else we can print statement inside function only
# we can give values as a global variable as well


# Task 9: Functional Pipeline Design
# Requirement: Create three small functions: clean_input(), apply_discount(), and
# format_currency().
# Task: Write a "Master" function process_invoice that pipes data through all three.
# Evaluation: The candidate must justify why using Tuples to pass data between these
# functions is safer than using Global Variables.

def clean_input(value):
    return value.strip()

def apply_discount(data_tuple):
    value = float(data_tuple[0])
    discounted = value * 0.9
    return (discounted,)

def format_currency(data_tuple):
    return f"${data_tuple[0]:.2f}"


def process_invoice(value):
    step1 = clean_input(value)
    step2 = apply_discount(step1)
    step3 = format_currency(step2)

    return step3

print(process_invoice("100"))
print(process_invoice(" 250 "))
print(process_invoice("500"))

# Task 10: The Fail-Safe Dispatcher
# Analogy: If a transaction fails, the system shouldn't crash; it should return a "Fail State"
# and a reason.
# Requirement: Create a function dispatch_payment that returns a Tuple
# (Success_Bool, Error_Message_Or_None).
# Logic: If Success_Bool is False, the second element must be a string. If True, the second
# element must be None.
# Documentation: Write a docstring explaining this specific "Result Pattern" (similar to
# Rust or Go error handling).

def dispatch_payment(amount):
    if amount <= 0:
        return (False, "Invalid payment amount")

    if amount > 5000:
        return (False, "Amount exceeds transaction limit")

    return (True, None)

print(dispatch_payment(1000))
print(dispatch_payment(6000))
print(dispatch_payment(-50))