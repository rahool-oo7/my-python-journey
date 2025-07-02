# 05_greatest_of_three.py
# ----------------------------------------
# Function to find the greatest among three numbers

def greatest(a, b, c=1):
    """
    Returns the greatest among three numbers.
    If no single number is greatest, returns a message.
    """
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    elif (c > a) and (c > b):
        return c
    else:
        return "No one is Greater"

# Input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Output the result
print("Greatest:", greatest(a, b, c))
