# 01_basic_python_assignment.py
# -------------------------------------------------------
# Assignment: Python Basics - Conditionals, Functions, File, Loops
# Author: Ritesh Kumar
# Description: A self-assessment assignment given by ChatGPT

import random
import time

# ---------- Q1: Even or Odd ----------
a = int(input("Enter a number: "))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# ---------- Q2: Age Group Classifier ----------
age = int(input("\nEnter your age: "))
if age < 13:
    print("Child")
elif 13 <= age < 20:
    print("Teenager")
elif 20 <= age < 60:
    print("Adult")
else:
    print("Senior")

# ---------- Q3: List Manipulation ----------
fruits = ["apple", "guava", "banana", "orange", "grapes"]
fruits.append("mango")    # Add new fruit
fruits.pop(1)             # Remove second fruit (guava)
fruits.sort()             # Sort alphabetically
print("\nSorted Fruit List:", fruits)

# ---------- Q4: Function to Greet User ----------
def greet_user(name):
    print(f"Hello, {name}!")

name = input("\nEnter your name: ")
greet_user(name)

# ---------- Q5: Dice Roll ----------
dice = random.randint(1, 6)
print(f"\nDice Rolled.... and it's a {dice}!")

# ---------- Q6: File Write & Read ----------
with open("files.txt", "w") as f:
    f.write("Python is awesome!")

with open("files.txt", "r") as f:
    content = f.read()
    print("\nFile Content:", content)

# ---------- BONUS Q7: Multiple Dice Rolls with Average ----------
total = 0
n = int(input("\nEnter number of times you want to roll the dice: "))
for i in range(1, n + 1):
    roll = random.randint(1, 6)
    print(f"Roll {i}: {roll}")
    total += roll
    time.sleep(1)

print("\nTotal:", total)
print("Average:", round(total / n, 2))
