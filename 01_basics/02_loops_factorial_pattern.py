# 02_loops_factorial_pattern.py
# -----------------------------------
# This script demonstrates:
# - Looping through a list to greet names with 'S' or 's'
# - Calculating factorial using a for loop
# - Printing a pyramid pattern using nested loops

# ---------- GREET NAMES STARTING WITH 'S' ----------
names = ["Harry", "Sohan", "sachin", "Rahul"]

# Greet only those whose name starts with 'S' or 's'
for name in names:
    if name.lower().startswith("s"):
        print(f"Hello {name}")

# ---------- FACTORIAL CALCULATION ----------
# Input from user
num = int(input("Enter a number to calculate factorial: "))
factorial = 1

# Multiply numbers from 1 to num
for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")

# ---------- PYRAMID STAR PATTERN ----------
# Input for number of rows
n = int(input("Enter the number of rows for pyramid pattern: "))

# Loop to print pyramid pattern
for i in range(1, n + 1):
    # Print leading spaces
    print("  " * (n - i), end="")
    # Print stars (2*i - 1) gives odd numbers: 1, 3, 5, ...
    print("* " * ((2 * i) - 1))
