# 19_digit_sum_divisible_filter.py
# ------------------------------------------------------------------------
# This script filters and prints all numbers from a list that are divisible
# by the sum of their digits (Harshad/Niven numbers).

# Function to calculate sum of digits
def sum_of_digits(num):
    return sum(int(d) for d in str(num))

# Input list of numbers
numbers = [132, 122, 788, 120, 840]

# List comprehension to filter Harshad numbers
result = [i for i in numbers if i % sum_of_digits(i) == 0]

# Output
print("Harshad (digit-divisible) numbers:")
print(result)
