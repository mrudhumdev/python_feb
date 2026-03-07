# Session – 6
# Phase 1: Application & Analysis
# Task 1: The Secure Data Scrubber (String Iteration)

#  Task: Take a string of characters. Iterate through it to create a new string that removes all
# special characters and numbers, keeping only alphabets.
#  Requirement: Use a for loop and the .isalpha() method. If a character is a space, use
# pass to maintain the gap.
input1 = "Alpha_User 101! #Beta$ & Gamma_99"
clean=""
for i in input1:
    if i.isalpha():
        clean+=i
    elif i==" ":
        clean+=" "
print(clean)


# Task 2: Financial Threshold Monitor (List Iteration)
# Context: Monitoring a list of stock prices: 

prices = [120.5, 118.2, 122.0, 115.5,125.0]

# Task: Iterate through the prices. Calculate the percentage change between the first price
# and every subsequent price.
# Action: If a price drops by more than 5% from the starting price, print a "SELL ALERT"
# and the index of that price.
start=prices[0]
for i in range(1, len(prices)):
    change = ((start - prices[i]) / start) * 100

    if change > 5:
        print(f"SELL ALERT at index {i}")


# Task 3: The API Response Validator (Dict Iteration)
# Context: You receive a dictionary of 
service_status= {"Auth": "200 OK", "Cache":"500 Error", "Database": "200 OK", "Proxy": "404 Not Found"}
# Task: Iterate through the dictionary using .items().
# Logic: For any status containing "200", print "Service Healthy". For any other status,
# print "Service Critical" and use the continue keyword to skip any further logging for
# that specific service.
for service, status in service_status.items():
    if "200" in status:
        print(f"{service}: Service Healthy")
    else:
        print(f"{service}: Service Critical")
        continue


# Task 4: The Smart Search Optimizer (For + Break)
#  Context: You are searching a massive list for a "target_id".
#  Task: Create a list of 20 random integers. Ask the user for a search value.
#  Action: Iterate through the list. Print "Analyzing index [i]...". Use break to stop the
# search the moment the value is found.
#  Analysis: After the loop, print a message indicating whether the search was efficient
# (stopped before the end) or exhaustive (checked every element).

# user_input = int(input("Enter number between 1 to 20: "))

# num = [1,2,3,4,5,6,7,8,9,10,
#        11,12,13,14,15,16,17,18,19,20]

# found = False

# for value in num:
#     print(f"Analyzing value {value}")

#     if value == user_input:
#         print("Target Found")
#         found = True
#         break

# if found:
#     print("Efficient Search")
# else:
#     print("Exhaustive Search")


# Task 5: Infinite Command-Line Interface (While + Exit)
# Context: Building a system utility menu.
# Task: Create an infinite while True loop.
# Action: Prompt user for commands: status, reset, or exit.
# Logic: Use a match-case (from Module 5) inside the while loop to handle the
# commands. Only the exit command should trigger the break keyword.

# while True:
#     cmd = input("Enter command (status/reset/exit): ")

#     match cmd:
#         case "status":
#             print("System Running")
#         case "reset":
#             print("System Reset")
#         case "exit":
#             print("Exiting...")
#             break
#         case _:
#             print("Unknown Command")


# Task 6: The Multi-Dimensional Grid Mapper (Nested Loops)
# Context: Generating a coordinate system for a game board (5x5).
# Task: Use nested for loops to print coordinates in the format (row, col).
# Requirement: Skip the "center" coordinate (2, 2) using the continue keyword in the
# inner loop.

for i in range(5):
    for j in range(5):
        if i==2 and j==2:
            continue
        print(f"({i},{j})") 


# Task 7: Resource Management Simulator (Control Keywords)
# Context: A battery charging simulator.
# Task: Start a while loop at battery = 0. Increment by 5.
# Logic: When battery reaches 20, 40, and 60, use print to show "Charging...". When it
# reaches 80, use pass (placeholder for "Slow Charge Mode"). When it hits 100, use break
# to stop and print "Fully Charged".

battery=0
while True:
    battery+=5
    if battery in [20,40,60]:
        print("charging")
    if battery == 80:
        pass
    if battery == 100:
        print("Fully Charged")
        break


# Task 8: The "Dirty Data" Integrator
# Scenario: You are processing a sensor log: logs = [22, 25, "TIMEOUT", 28, 0,
# "ERROR", 30].
# Problem: You need the average temperature, but "TIMEOUT" should be ignored, 0
# should be ignored as a false reading, and "ERROR" indicates a catastrophic failure where
# no further data should be processed.
# Challenge: Write a loop that calculates the sum and count of valid temperatures. Use
# continue for "TIMEOUT" and 0, and break for "ERROR". Print the final average of the
# data processed up to the error.

logs = [22, 25, "TIMEOUT", 28, 0, "ERROR", 30]

total = 0
count = 0
for i in logs:

    if i == "TIMEOUT" or i == 0:
        continue
    if i == "ERROR":
        break

    total += i
    count += 1

if count > 0:
    print("Average:", total / count)


# Task 9: The Prime Number Architect
# Challenge: Write a script to find all prime numbers between 2 and 50.
# Logic: You must use a nested loop structure. The outer loop picks the number, and the
# inner loop tests for divisibility.
# Evaluation: Optimize your loop using a break keyword so that as soon as a factor is
# found, the inner loop stops checking. Explain in a comment why this is more "efficient"
# than checking every number.

for num in range(2, 50):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# break makes it efficient because the loop stops
# immediately when a factor is found instead of
# checking all remaining numbers.


# Task 10: State-Machine Transaction Logic Scenario: A vending machine script. balance =
# 50. items = {"Soda": 15, "Chips": 10, "Candy": 5}.
# Task: Create a loop that allows a user to buy items until their balance is too low or they
# type "finished".
# Constraint: 1. If the user picks an item they can't afford, use continue to let them pick
# something else.
# 2. If the balance reaches 0, use break automatically.
# Critical Thinking: Add a pass statement in a section where you would theoretically
# "Refund" money, then explain in the submission why you chose that structure for future
# scalability

balance = 50
items = {"Soda": 15, "Chips": 10, "Candy": 5}

while True:

    print("Balance:", balance)
    choice = input("Select item or type finished: ")

    if choice == "finished":
        pass
        # Future: refund logic can be added here
        break

    if choice not in items:
        continue

    if items[choice] > balance:
        print("Cannot afford")
        continue

    balance -= items[choice]
    print(f"Purchased {choice}")

    if balance == 0:
        break


    # pass is used as a placeholder for future refund logic.
# This keeps the structure ready for scalability
# without breaking current flow.


