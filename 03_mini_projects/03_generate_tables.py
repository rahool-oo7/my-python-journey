# 03_generate_tables.py
# ------------------------------------------------------------
# Mini Project: Multiplication Table Generator (No os module)
# This script generates tables from 1 to 10 and saves them into
# separate text files under an existing 'tables' folder.

def generate_table(n):
    """
    Generates multiplication table of `n` and writes it to a text file.
    Assumes 'tables/' folder already exists.
    """
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

    # Write the table to a file inside the 'tables' folder
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables from 1 to 10
for i in range(1, 11):
    generate_table(i)
