# Session – 4
# Task 1: The "Safe Lookup" Dictionary Engine

# 1. Data Setup: Create a dictionary named inventory with the following initial data:

inventory={"sku_01": 50, "sku_02": 150, "sku_03": 75}

# 2. Operations:
# o Use the .update() method to add a new item "sku_04" with a value of 200.

inventory.update({"sku_04":200})
print(inventory)

# o Retrieve the value for "sku_02" using direct bracket notation.

print(inventory["sku_02"])

# o Use the .get() method to search for "sku_05". Provide a default return value of
# to handle the missing key safely.

get_value=inventory.get("sku_05", 0)
print(f"the get values of dictionary are : {get_value}")

# 3. Analysis: Use .keys() and .values() to print the list of all IDs and the list of all stock
# counts respectively.

key=inventory.keys()
print(f"the keys of dictionary are : {key}")
value=inventory.values()
print(f"the values of dictionary are : {value}")

# 4. Transformation: Print the dictionary as a list of tuples using the .items() method.

item=inventory.items()
print(f"the items of dictionary are : {item}")

# Task 2: Deep Access in Nested JSON-like Structures

# 1. Data Setup: Create a variable named api_response that mimics a JSON object:

api_response = {
"status": "success",
"data": [
{"id": 1, "info": {"email": "user1@work.com", "tags": ["admin",
"dev"]}},
{"id": 2, "info": {"email": "user2@work.com", "tags":
["guest"]}}
]
}

# 2. Extraction Challenge: * Access the email of the first user in the list and store it in
# user_1_email.

user_1_email=api_response["data"][0]["info"]["email"]
print(f"User 1 details: {user_1_email}")



# o Access the second tag of the first user ("dev") and store it in
# user_1_secondary_tag.

user_1_secondary_tag = api_response["data"][0]["info"]["tags"][1]
print(f"user secondary tag: {user_1_secondary_tag}")

# o Retrieve the ID of the last user in the list using negative indexing.

last_user_id = api_response["data"][-1]["id"]
print(f" last user id: {last_user_id}")

# 3. Observation: Print the type() of api_response["data"] and
# api_response["data"][0]["info"].

print(type(api_response["data"])) 
# tha class is list
print(type(api_response["data"][0]["info"]))
# this is dictionary

# Task 3: String Sanitization & Cleaning Pipeline
# Objective: Perform industrial-strength string cleaning using .strip(), .replace(), and
# .find().
# 1. Raw Data: Create a string: 

raw_log = " ERROR_CODE: 404 | STATUS: NOT_FOUND |SOURCE: SERVER_01 "

# 2. The Pipeline:
# o Remove the leading and trailing whitespace using .strip().

whitespace=raw_log.strip()
print(f" Removing the whitespace:{whitespace}")

# o Replace all underscores (_) with spaces.

replace=raw_log.replace("_"," ")
print(f" Repcaing function :{replace}")
# o Use the .find() method to locate the index of the vertical bar |.

index_loc=raw_log.find("|")
print(f" Finding index value of | is :{index_loc}")

# o Convert the entire string to lowercase for uniform processing.

lower=raw_log.lower()
print(f" lower case of raw_log :{lower}")

# 3. Verification: Print the final "cleaned" version of the log.
cleaned_log = raw_log.strip()
cleaned_log = cleaned_log.replace("_", " ")
cleaned_log = cleaned_log.lower()

print(cleaned_log)


# Task 4: The CSV-to-Python Parser (Split & Join)

csv_data ="Apple,iPhone,1200,Silver"

# o Use .split(",") to turn this into a list called product_details.

product_details=csv_data.split(",")
print(product_details)

# 2. Modification: Change the price (at index 2) to "1300".

product_details[2]="1300"
print(product_details)

# 3. Reconstruction: Use the .join() method to convert the list back into a single string, but
# use a semicolon (;) as the new separator.

new_csv = ";".join(product_details)
print(new_csv)

# 4. Header Generation: Create a header string "BRAND;MODEL;PRICE;COLOR" and
# concatenate it with your reconstructed string, separated by a newline character (\n).

header="BRAND;MODEL;PRICE;COLOR"
output=header + "\n" +new_csv
print(output)

# Task 5: Atomic Dictionary Merging & Popping
# Objective: Advanced dictionary methods for data management.
# 1. Merging: Create two dictionaries:

personal_info = {"name": "John", "age": 30}
job_info = {"salary": 5000, "role": "Analyst"}

# o Use the Dictionary Union Operator (|) to merge them into a new dictionary
# called full_profile.

full_profiles=personal_info | job_info
print(f"merge two dictionaries: {full_profiles}"
      )
# 2. Extraction: Use the .pop() method to remove the "age" key from full_profile and
# store the removed value in a variable called removed_age.
removed_age=full_profiles.pop("age")
print(f"removed age : {removed_age}")

# 3. Clearing: Use the .clear() method on the personal_info dictionary. Print its length
# to prove it is now empty.
full_profiles.clear()
print(len(full_profiles))
