# 09_copy_file_content.py
# ------------------------------------------------------------
# This basic script copies the content of one file (pehla.txt)
# and writes it into another file (dusra.txt)

# Open and read content from the source file
# Make sure 'pehla.txt' exists in the same directory with some content
with open("pehla.txt", "r") as f:
    content = f.read()

# Write the same content to the destination file
with open("dusra.txt", "w") as f:
    f.write(content)

print("File content copied from pehla.txt to dusra.txt successfully.")
