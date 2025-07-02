# 01_snake_water_gun.py
# ---------------------------------------------------
# Mini Project 1: Snake, Water, Gun Game
# User plays against the computer.
# Snake drinks Water, Water drowns Gun, Gun kills Snake.

import random

# Mapping moves to integers and vice versa
gameDict = {-1: "Snake", 0: "Water", 1: "Gun"}
revGameDict = {"s": -1, "w": 0, "g": 1}

# Random move for computer
Computer = random.choice([-1, 0, 1])

# User input
User = input("Enter your move (s for Snake, w for Water, g for Gun): ").lower()

# Check for valid input
if User not in revGameDict:
    print("Invalid input. Please enter 's', 'w', or 'g'.")
else:
    UserMove = revGameDict[User]
    
    # Show choices
    print(f"Computer chose: {gameDict[Computer]}")
    print(f"You chose: {gameDict[UserMove]}")

    # Determine result
    if Computer == UserMove:
        print("It's a Draw!")

    # Winning conditions for computer
    elif (Computer == -1 and UserMove == 0) or \
         (Computer == 0 and UserMove == 1) or \
         (Computer == 1 and UserMove == -1):
        print("Computer Wins!")

    else:
        print("You Win!")
