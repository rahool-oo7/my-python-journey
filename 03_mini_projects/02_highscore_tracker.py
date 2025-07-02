# 02_highscore_tracker.py
# -------------------------------------------------------
# Mini Project: High Score Tracker
# Randomly generates a score between 1 and 100
# Compares it with a saved high score in a text file
# Updates the file if the current score is higher

import random

# Generate a random score between 1 and 100
score = random.randint(1, 100)

# Read current high score from file
try:
    with open("HighScore.txt", "r") as f:
        content = f.read().strip()
        highscore = int(content) if content.isdigit() else 0
except FileNotFoundError:
    highscore = 0  # If file doesn't exist yet

# Compare and update if needed
if score > highscore:
    with open("HighScore.txt", "w") as f:
        f.write(str(score))
    print(f"🎉 New High Score: {score}")
else:
    print(f"Current Score: {score}")
    print(f"High Score: {highscore}")
