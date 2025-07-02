# 18_walrus_operator_example.py
# -------------------------------------------------------------------
# This script accepts numbers from the user until 0 is entered.
# It stores only positive numbers in a list and prints them at the end.

positive_numbers = []

# Loop to keep taking input until 0 is entered
while (num := int(input("Enter a number (0 to stop): "))) != 0:
    if num > 0:
        positive_numbers.append(num)

# Print the list of positive numbers
print("\nList of positive numbers entered:")
print(positive_numbers)
