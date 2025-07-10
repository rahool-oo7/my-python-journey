# 27_missing_characters_filter.py
# ------------------------------------------------------------------------
# This script compares a given string with the full set of digits (0-9) and
# lowercase alphabets (a-z), and prints characters that are missing from
# the input. This helps identify unused or skipped characters.

def find_missing_characters(typed):
    original = "0123456789abcdefghijklmnopqrstuvwxyz"
    typed_set = set(typed)
    missing = ""

    for char in original:
        if char not in typed_set:
            missing += char

    print("Missing characters:", missing)

# Test
typed = "8hypotheticall024y6wxz"
find_missing_characters(typed)
