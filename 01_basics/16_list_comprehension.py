# 16_list_comprehension.py
# ----------------------------------------------------------------
# This script generates a multiplication table using list comprehension
# and appends the result to a file named 'tableNew.txt'

# Input a number
n = int(input("Enter the number: "))

# Generate multiplication table from 1 to 10
table = [n * i for i in range(1, 11)]

# This script appends the table to 'tableNew.txt'
# Note: 'tableNew.txt' is an output file and is not included in version control.
with open("tableNew.txt", "a") as f:
    f.write(f"Table of {n}: {table}\n")

print(f"Multiplication table of {n} written to tableNew.txt")
