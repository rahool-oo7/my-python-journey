# 20_table_and_filter_by_five.py
# -----------------------------------------------------------------------
# This script does two things:
# 1. Prints the 7-times multiplication table (1 to 10)
# 2. Filters and prints numbers divisible by 5 from a list

# ----------- PART 1: 7 Times Table -----------
table = [str(i * 7) for i in range(1, 11)]
print("7 Times Table:")
print("\n".join(table))


# ----------- PART 2: Filter Numbers Divisible by 5 -----------

# Function to check divisibility by 5
def is_divisible_by_5(n):
    return n % 5 == 0

# List of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 15, 65]

# Apply filter
result = list(filter(is_divisible_by_5, numbers))

# Output result
print("\nNumbers divisible by 5:")
print(result)
