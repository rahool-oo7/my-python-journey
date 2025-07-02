# 03_hollow_square_pattern.py
# -----------------------------------
# This script prints a hollow square pattern of size n x n using stars (*).
# The first and last rows are filled with stars.
# The middle rows have stars only on the borders.

# Input: Size of the square
n = int(input("Enter the number: "))

# Loop through each row
for i in range(1, n + 1):
    if i == 1 or i == n:
        # First and last row: full row of stars
        print("* " * n, end="")
    else:
        # Middle rows: star + spaces + star
        print("* ", end="")                # Left border
        print("  " * (n - 2), end="")      # Hollow space
        print("* ", end="")                # Right border
    print("")  # New line after each row
