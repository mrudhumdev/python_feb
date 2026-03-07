# Session – 5
# Task 1: The "Truthy/Falsy" Validation Suite
# Objective: Understand how Python evaluates non-boolean types in a boolean context.
# 1. Variable Setup: Create the following variables:
val_1 = 0
print(type(val_1))
val_2 = 0.0
print(type(val_2))
val_3 = "" 
val_4 = None
val_5 = "False" 

print(type(val_3))
print(type(val_4))
print(type(val_5))

# 2. Logic Test: Write an if-else block for each variable to check if Python considers it
# True or False.
# 3. Output: Print a formatted message for each: "Variable [X] with value [Y] is
# evaluated as [TRUE/FALSE]".
if val_1:
    print(f"the value1 {val_1} is True")
else:
    print(f"the value1 {val_1} is False")

# 
if val_2:
    print(f"the value2 {val_2} is True")
else:
    print(f"the value2 {val_2} is false")

# 
if val_3:
    print(f"the value2 {val_3} is True")
else:
    print(f"the value2 {val_3} is false")

# 
if val_4:
    print(f"the value2 {val_4} is True")
else:
    print(f"the value2 {val_4} is false")

# 
if val_5:
    print(f"the value2 {val_5} is True")
else:
    print(f"the value2 {val_5} is false")



# 4. Analysis: In a comment, explain why val_5 evaluates differently than the others.

# val_5 evaluates as TRUE because it is a non-empty string.
# Python treats any non-empty string as True in boolean context,
# even if the text inside the string is "False".


# Task 2: Multi-Tiered Logical Branching (The Tax Engine)
# Objective: Implement a professional if-elif-else structure with nested logic.
# 1. Input: Prompt a user for their annual_income (float) and residency_status (string:
# "Resident" or "Non-Resident").

# annual_income = float(input("Enter your annual income: "))
# residency_status = input("Enter residency status (Resident/Non-Resident): ")
annual_income=50000
residency_status="Resident"
# 2. The Logic:
# o If annual_income is less than or equal to 30,000, tax is 0%.
# o If annual_income is between 30,001 and 80,000:
#  Residents pay 10%.
#  Non-Residents pay 15%.
# o If annual_income is above 80,000, everyone pays 25%.
if annual_income <= 30000:
    tax=0
elif 30001< annual_income <=80000:
    if residency_status=="Resident":
        tax=0.10
    else:
        tax=0.15
elif annual_income>80000:
    tax=0.25

# 3. Calculation: Calculate the tax_amount and the remaining_balance.

tax_amount = annual_income * tax
remaining_balance = annual_income - tax_amount

# 4. Output: Use f-strings to print a summary including the income, the applied tax rate, and
# the final balance.

print(f"tax amount: {tax_amount}")
print(f"remaining balance: {remaining_balance}")

# Task 3: Modern Pattern Matching (match-case)
# Objective: Replace traditional switch-case logic with Python's match-case for cleaner code.
# 1. Scenario: You are building a system that processes "HTTP Status Codes."

# 2. The Task: Create a variable status_code (int) via user input.
status_code = int(input("Enter HTTP status code(200/400/404/500): "))
# 3. Implementation: Use a match status_code: block to handle:
# o 200 -> Print "Success: OK"
# o 400 -> Print "Client Error: Bad Request"
# o 404 -> Print "Client Error: Not Found"
# o 500 -> Print "Server Error: Internal Server Error"
# o Wildcard (_): Handle any other code by printing "Unknown Status Code".
match status_code:
    case 200:
        print("Success: OK")
    case 400:
        print("Client Error: Bad Request")
    case 404:
        print("Client Error: Not Found")
    case 500:
        print("Server Error: Internal Server Error")
    case _:
        print("Unknown Status Code")


# Task 4: Structural Pattern Matching with Combined Patterns
# Objective: Use the pipe operator (|) in match-case to group multiple conditions.
# 1. Scenario: A file processing system accepts different extensions.
# 2. The Task: Create a variable file_ext (string) via user input (e.g., ".jpg", ".png", ".pdf").
file_ext = input("""Enter file extension (e.g., ".jpg", ".png", ".pdf"): """)

# 3. Implementation: Use a match statement to categorize the file:
# o If ".jpg", ".jpeg", or ".png" -> Print "File Type: Image"
# o If ".pdf", ".docx", or ".txt" -> Print "File Type: Document"
# o If ".mp4" or ".mkv" -> Print "File Type: Video"
# o Case _ -> Print "File Type: Unsupported"

match file_ext:
    case ".jpg" | ".jpeg" | ".png":
        print("File Type: Image")

    case ".pdf" | ".docx" | ".txt":
        print("File Type: Document")

    case ".mp4" | ".mkv":
        print("File Type: Video")

    case _:
        print("File Type: Unsupported")


# Task 5: The "Short-Circuit" Logic Challenge
# Objective: Combine if statements with Logical Operators (and, or, not) to manage access.
# 1. Scenario: A system requires three flags for "System Override" access:
# o is_admin (bool)
is_admin=bool(input("are you admin: "))
# o has_security_key (bool)
has_security_key=bool(input("do you have security key: "))
# o system_offline (bool)
system_offline=bool(input("is system offline: "))
# 2. The Task: Set these variables using input() and type casting to bool. (Note: In Python,
# bool(input()) might be tricky—ensure you compare the input string to "True").
# 3. Requirement: A user is granted "OVERRIDE ACCESS" only if:
# o They are an admin AND have the security_key.
# o OR if the system_offline flag is True (regardless of admin status).

# 4. Execution: Use one if-else block to determine access and print the result.
if (is_admin and has_security_key) or system_offline:
    print("OVERRIDE ACCESS GRANTED")
else:
    print("ACCESS DENIED")