
# Session – 2


# Task 1: The "Identity vs. Equality" Investigation
# 1. Memory Mapping: Create two variables x = 256 and y = 256. Print their memory
# addresses using id().
x=256
y=256
print(id(x))
print(id(y))

# 2. The Cache Limit: Create two more variables a = 257 and b = 257. Print their memory
# addresses.
a=int("257")
print(id(a))
b=int("257")
print(id(b))


# 3. Boolean Identity: Create a variable is_same_identity that stores the result of a is b
# and is_same_value that stores a == b.
is_same_identity= a is b
print(is_same_identity)

is_same_value=(a==b)
print(is_same_value)


# 4. NoneType Check: Assign status = None. Print its type() and its memory address.
status=None
print(type(status))
print(id(status))

# 5. Output: Use a single f-string to display the id() of all variables and the boolean results
# of your identity tests.
print(f"the memory address of {a} and {b} is {is_same_identity}")
print(f"the memory address of {a} and {b} is {is_same_value}")


# Task 2: Advanced I/O and Type Casting Pipeline

# 1. User Acquisition: Use input() to collect:
# o hourly_rate (Expected: Float)
# o hours_worked (Expected: Int)
# o tax_bracket (Expected: Float, e.g., 0.2 for 20%)
# 2. Casting: Cast these inputs directly into their respective types.
# 3. Calculation: Calculate the gross_pay and the net_pay (Gross - (Gross * Tax)).
# 4. Validation: Print the type() of each processed variable to ensure the casting was
# successful.

# hourly_rate = float(input("Enter hourly rate: "))
# hours_worked = int(input("Enter hours worked: "))
# tax_bracket = float(input("Enter tax bracket (e.g., 0.2 for 20%): "))


# gross_pay = hourly_rate * hours_worked
# net_pay = gross_pay - (gross_pay * tax_bracket)

# print(f"hourly_rate_type:{type(hourly_rate)}")
# print(f"hourly_rate_type:{type(hours_worked)}")
# print(f"hourly_rate_type:{type(tax_bracket)}")

# print(f"gross_pay type: {type(gross_pay)} ,net_pay type: {type(net_pay)}")
# print(f"Gross Pay: {gross_pay} ,Net Pay: {net_pay}")

# Task 3: Precision Engineering with F-Strings

# 1. Design Requirements: Using the data from Task 2, print a "Salary Statement" with the
# following constraints:
# o Header: A string "OFFICIAL PAYSLIP" centered in a 40-character block using = as a filler.
# o Labels: All labels (e.g., "Hourly Rate:") must be left-aligned with a width of 25.
# o Values: All numerical values must be right-aligned, fixed to 3 decimal places,
# and preceded by a currency symbol.
# 2. Visual Structure: Use string multiplication to create a divider line that exactly matches
# the width of your header.

# Header
# header = f"{'OFFICIAL PAYSLIP':=^40}"

# # Divider using string multiplication
# divider = "-" * 40
# # ->	filler , ^	-> center align , 40 ->	total width
# print(header)
# print(divider)

# print(f"{'Hourly Rate:':<25}${hourly_rate:>14.3f}")
# print(f"{'Hours Worked:':<25}${hours_worked:>14.3f}")
# print(f"{'Tax Bracket:':<25}${tax_bracket:>14.3f}")
# print(f"{'Gross Pay:':<25}${gross_pay:>14.3f}")
# print(f"{'Net Pay:':<25}${net_pay:>14.3f}")

# <   right allign
# >	right align
# 14	width
# .3f	3 decimal places
# $	currency symbol

# print(divider)


# Task 4: Complex Expressions & Operator Precedence

# 1. The Formula: Implement the following expression in Python:
# (Note: Use a=10, b=5, c=2, d=3, e=2, f=8, g=3)
# 2. Evaluation: Predict the result manually based on Python’s precedence rules (Parentheses
# > Exponent > Multiplicative > Additive).
# 3. Logical Layer: Create a boolean variable is_valid that checks if the Result is greater
# than 0 AND Result is not equal to None.
# 4. Verification: Print the final Result and the is_valid status.

a = 10
b = 5
c = 2
d = 3
e = 2
f = 8
g = 3


result = (a + b) * c ** d - e / f + g

is_valid = result > 0 and result is not None

print(f"Final Result: {result} , Is Valid: {is_valid}")



# Task 5: Bitwise Permissions & Flag Manipulation

# 1. Define Flags: Assume a system security bit-mask:
# o GUEST = 1 (0001)
# o USER = 2 (0010)
# o ADMIN = 4 (0100)
# o SUPERUSER = 8 (1000)
# 2. Operations:
# o Combine: Create a current_access variable that combines GUEST and USER
# using the OR (|) operator.
# o Elevate: Use the Left Shift (<<) operator to double the value of the ADMIN flag
# and store it as NEW_SECURE_LEVEL.
# o Check: Use the AND (&) operator to verify if current_access contains the USER bit.
# o Toggle: Use the XOR (^) operator to remove the GUEST permission from
# current_access.
# 3. Binary Output: Print all results in both decimal and binary (using bin()) to see the bit
# transitions.
GUEST=1
USER=2
ADMIN=4
SUPERUSER=8
current_variable= GUEST | USER
NEW_SECURE_LEVEL= ADMIN<<1
permission= current_variable & USER
xor= current_variable ^ GUEST

print(f"GUEST: {GUEST} , {bin(GUEST)}")
print(f"USER: {USER} , {bin(USER)}")
print(f"ADMIN: {ADMIN} , {bin(ADMIN)}")
print(f"SUPERUSER: {SUPERUSER} , {bin(SUPERUSER)}")

print(f"or operation : {current_variable} , {bin(current_variable)}")
print(f"left shift operation : {NEW_SECURE_LEVEL} , {bin(NEW_SECURE_LEVEL)}")
print(f"and operation : {permission} , {bin(permission)}")
print(f"xor operation : {xor} , {bin(xor)}")


