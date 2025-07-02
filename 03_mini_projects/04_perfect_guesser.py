# 04_perfect_guesser.py
# ---------------------------------------------------------------------
# Mini Project: Perfect Guesser 🎯
# The user must guess a randomly generated number between 1 and 100.
# Feedback is given after each guess, and total attempts are tracked.

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize guess and attempt counter
guess = -1
guesses = 0

print("🎮 Welcome to the Perfect Guesser Game!")
print("Try to guess the number between 1 and 100.\n")

# Game loop
while guess != secret_number:
    guess = int(input("Guess the number: "))
    guesses += 1

    if guess > secret_number:
        print("📉 Lower")
    elif guess < secret_number:
        print("📈 Higher")

# Winning message
print(f"\n✅ You guessed correctly! The number was {secret_number}.")
print(f"🔢 Total number of guesses: {guesses}")
