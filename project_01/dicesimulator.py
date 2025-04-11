#Simulate rolling two dice, three times. 
# Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 : int = random.randint(1, 6)
    die2 : int = random.randint(1, 6)
    total : int = die1 + die2
    print("Total of two dice: ", total)

def main():
    """
    Demonstrates variable scope by rolling dice multiple times while tracking a local variable.
    """
    die1 : int = 0
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() ends as: " + str(die1))

if __name__ == "__main__":
    main()
