# 15_enumerate_selected_items.py
# ---------------------------------------------------------------------
# This script demonstrates use of enumerate() to access both index and item
# It prints the 3rd, 5th, and 7th items from the list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index, item in enumerate(l):
    if index in [2, 4, 6]:  # Select specific indices
        print(f"{index + 1} item is: {item}")
