# 04_recursive_factorial.py
# --------------------------------------
# This script calculates the factorial of a number using recursion.
# It also prints the recursive steps for better understanding.

# Function to calculate factorial recursively
def factorial(n):
    print(f"Calculating factorial({n})")
    
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive call
    result = n * factorial(n - 1)
    print(f"{n} * factorial({n-1}) = {result}")
    return result

# Input from user
n = int(input("Enter the number: "))

# Calculate and print factorial
result = factorial(n)
print("Factorial:", result)
