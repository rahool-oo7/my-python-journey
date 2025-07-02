# 08_replace_word_in_file.py
# ----------------------------------------------------------------
# This basic script replaces all case-insensitive occurrences of the word "donkey"
# in the file "donkey.txt" with the word "Elephant"

import re

# Word to replace
word_to_replace = "donkey"

# Read the file content
with open("basics/inputs/donkey.txt") as f:
    content = f.read()

# Replace all whole-word matches (case-insensitive)
updated_content = re.sub(rf"(?i)\b{word_to_replace}\b", "Elephant", content)

# Overwrite the original file with updated content
with open("basics/inputs/donkey.txt", "w") as f:

    f.write(updated_content)

print("Replaced all occurrences of 'donkey' with 'Elephant'.")
