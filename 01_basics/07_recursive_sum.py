# 07_recursive_sum_and_strip.py
# ------------------------------------------------
# This script demonstrates:
# - Recursively summing the first 'n' natural numbers
# - Using the strip() method on a string

# ---------- RECURSIVE SUM FUNCTION ----------
def sum_natural(n):
    """
    Recursively calculates the sum of first n natural numbers.
    Base case: Sum(1) = 1
    """
    if n == 1:
        return 1
    return n + sum_natural(n - 1)

# Input from user
num = int(input("Enter a number to find the sum of natural numbers: "))
print("Sum is:", sum_natural(num))

# ---------- STRING STRIP DEMO ----------
# Removes lowercase 'h' from the beginning and end of the string
string = "Hello" 
print("After strip('h'):", string.strip("h"))   #It won't remove 'H'
