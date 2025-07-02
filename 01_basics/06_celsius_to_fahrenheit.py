# 06_celsius_to_fahrenheit.py
# ----------------------------------------
# Converts temperature from Celsius to Fahrenheit

def celsius_to_fahrenheit(c):
    """
    Converts Celsius to Fahrenheit.
    Formula: (C * 9/5) + 32
    """
    return (c * 9 / 5) + 32

# Input from user
celsius = int(input("Enter temperature in Celsius: "))

# Output in Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit:", fahrenheit, "F")
