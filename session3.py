# Session – 3

# Task 1: Matrix Slicing and List Manipulation

# 1. Data Setup: Create a list named data_stream containing the integers from 0 to 20.
data_stream = list(range(21))
print("Original List:", data_stream)

# 2. Slicing Challenge: * Extract a sub-list of all even numbers in reverse order using a
# single slicing expression.
even_reverse = data_stream[::-2]
print("Even numbers reversed:", even_reverse)

# o Extract the middle five elements of the original list.

middle_five = data_stream[8:13]
print("Middle five elements:", middle_five)

# 3. Mutability Test: * Replace the elements at index 2 and 3 with the string "MODIFIED"
# using slice assignment.
data_stream[2:4] = ["MODIFIED", "MODIFIED"]


# o Append the value 99 to the end and insert 0.5 at the beginning.

data_stream.append(99)
data_stream.insert(0,0.5)
# print(data_stream)

# 4. Verification: Print the final list and its current length.
print(f"final list: {data_stream}")
print(f"length of list : {len(data_stream)}")


# Task 2: Immutable Records & Tuple Unpacking

# 1. The Record: Create a tuple representing a professional employee record: (101, "Alice
# Smith", "Data Engineer", "London").

employee = (101, "Alice Smith", "Data Engineer", "London")

# 2. Unpacking: Unpack this tuple into four distinct variables: emp_id, name, role, and
# location.

emp_id, name, role, location = employee
print(emp_id)
print(name)
print(role)
print(location)

# 3. Extended Unpacking: Create a larger tuple with 6 values. Use the "starred" expression
# (*) to unpack the first element into head, the last element into tail, and everything in
# between into a list called mid.

record = (1, 2, 3, 4, 5, 6)

head, *mid, tail = record

print("Head:", head)
print("Mid:", mid)
print("Tail:", tail)
# *mid values gives the remaining values 

# 4. Immutability Proof: Attempt to change the location inside the tuple. Wrap this line in
# a comment and explain the specific error Python would throw

employee = (101, "Alice Smith", "Data Engineer", "London")

# names.replace("london","America")
# It shows an attribute error tuple object has no attribute 'append'
#  but we can fetch the values in tuple
print(employee[0])

# tuple is a collection of data  which is ordered and immutable (cannot make changes)


# Task 3: Deduplication and Set Hashability

# 1. Cleaning Data: You are given a raw list of user IDs: [1001, 1002, 1001, 1005,
# 1003, 1002, 1008]. Convert this list into a set called unique_ids to automatically
# remove duplicates.

User_id=[1001, 1002, 1001, 1005,1003, 1002, 1008]
unique_id=set(User_id)
print(unique_id)

# 2. Immutability Constraint: Try to add a list (e.g., [1, 2]) as an element into your set. In
# a comment, explain why this causes a TypeError.

# unique_id.add([1,2])
# print(unique_id)
#  It throws an Type error cannot use list as a set element (unhashable type: list)
# since unique_id is converted into set its immutrable cannot make changes 
# so it throws an error

# 3. Set Growth: Use the .add() method to insert a new ID and the .update() method to
# add multiple IDs from another list: [1010, 1011].
unique_id.add(1009)
unique_id.update([1010, 1011])
print(f"NEW ID: {unique_id}")


# Task 4: Mathematical Set Operations

# 1. The Scenario: You have two groups of software skills:

frontend_devs = {"HTML", "CSS", "JS", "React", "Python"}
backend_devs = {"Python", "Java", "NodeJS", "Go", "JS"}


# 2. Operations:
# o Full Stack: Find all unique skills across both groups (Union).

full_stack = frontend_devs.union(backend_devs)
print(f"Union : {full_stack}")


# o Overlap: Find skills common to both groups (Intersection).

over_lap=frontend_devs.intersection(backend_devs)
print(f"Intersection: {over_lap}")

# o Specialists: Find skills that exist in backend_devs but NOT in frontend_devs
# (Difference).
specialists = backend_devs.difference(frontend_devs)
print(f" Difference: {specialists}")

# o Unique to One: Find skills that are in one group or the other, but not both
# (Symmetric Difference).
unique_to_one = frontend_devs.symmetric_difference(backend_devs)
print(f" Unique to one : {unique_to_one}")



# Task 5: The "Collection Conversion" Pipeline

# 1. The Flow: * Start with a Tuple of 5 floating-point numbers.
numbers= (3.5, 1.2, 4.8, 2.1, 3.5)
# o Convert that Tuple into a List to sort it in ascending order using a list method.

numbers_list=list(numbers)
print(f"numbers list : {numbers_list}")

# o Convert that List into a Set to check if adding a duplicate value changes the size.

numbers_set=set(numbers_list)
numbers_set.add(1.2)
#  if we add duplicate values the sixe of set doesnot change 
#  because set contains no duplicate values and unordered as well
print(f"numbers set : {numbers_set}")

# o Convert it back into a Tuple to ensure the final data is protected from further
# accidental changes.

numbers_tuple=tuple(numbers_set)
print(f" numbers tuple : {numbers_tuple}")

# 2. Memory Identity: Use id() to show that the List and the Set have different memory
# addresses even if they hold the same values.
print(f"ID of list : {id(numbers_set)}")
print(f"ID of set : {id(numbers_set)}")
# memory address of the list remains same 
#  but memory address of set changes for each and every time we run , 
# it gets different memory address every time










