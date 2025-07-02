# 17_zero_division_handling.py
# ----------------------------------------------------------------------
# This script demonstrates how to handle ZeroDivisionError using try-except
# It performs a / b with 2 decimal rounding, and handles division by zero gracefully

try:
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    
    # Perform division and round to 2 decimal places
    result = round(a / b, 2)
    print("A / B is:", result)

except ZeroDivisionError:
    print("❌ Division by zero is not allowed (infinite).")

except ValueError:
    print("❌ Please enter valid integers.")

print("✅ Thank you!")
