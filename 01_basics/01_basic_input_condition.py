# 01_basic_input_conditions.py
# ----------------------------------
# This script includes basic Python concepts:
# - String operations
# - List modification
# - Using sets to store unique input
# - Grading logic based on marks
# - Conditional checks using input and lists

# ---------- STRING OPERATIONS ----------
name_str = "Ritesh is a  Good boy"
# Find the double space
print("Index of double space:", name_str.find("  "))
# Replace double space with single space
print("After replacing double space:", name_str.replace("  ", " "))

# ---------- LIST OPERATIONS ----------
L1 = [1, 34, 62, 9, 56, 9]
# Removes first occurrence of 9
L1.remove(9)
print("Updated List:", L1)

# ---------- SET: UNIQUE NUMBER INPUT ----------
# Using a set to collect 8 unique numbers from user input
unique_numbers = set()
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    unique_numbers.add(num)
print("Unique numbers entered:", unique_numbers)

# ---------- MARKS & PASS/FAIL LOGIC ----------
# Taking 3 subject marks and calculating percentage
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))

total_percentage = ((m1 + m2 + m3) / 300) * 100

# Conditions to pass:
# - Each subject should be above 32 marks
# - Overall percentage should be >= 40%
if (m1 > 32) and (m2 > 32) and (m3 > 32) and (total_percentage >= 40):
    print(f"Student passed with {total_percentage:.2f}%")
else:
    print(f"Student failed with {total_percentage:.2f}%")

# ---------- NAME LENGTH & PRESENCE CHECK ----------
name = input("Enter your name: ")

# Check if name is less than 10 characters
if len(name) < 10:
    print("Name is less than 10 characters.")
else:
    print("Name is 10 or more characters.")

# Check if name exists in a predefined list
name_list = ["ritesh", "anushka", "vaibhav", "suraj"]
if name.lower() in name_list:
    print("Name is present in the list.")
else:
    print("Name is not present in the list.")
