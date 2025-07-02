# virtual_environment_starter.py
# ----------------------------------------------------------
# This script tests that all installed libraries work correctly

# These library should be installed in the current virtual environment
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# To run the program
# source venv/bin/activate
# python starter_program.py


# Numpy test
array = np.array([1, 2, 3])
print("Numpy Array:", array)

# Pandas test
df = pd.DataFrame({'Name': ['Ritesh', 'Anushka'], 'Score': [95, 88]})
print("\nPandas DataFrame:\n", df)

# Requests test
try:
    r = requests.get("https://api.github.com")
    print("\nGitHub API Status:", r.status_code)
except:
    print("Internet not available or request failed.")

# Matplotlib test
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Test Plot")
plt.savefig("test_plot.png")
print("\nMatplotlib plot saved as 'test_plot.png'")


