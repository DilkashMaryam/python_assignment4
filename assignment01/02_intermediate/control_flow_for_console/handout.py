"""A simple high-low guessing game where the player guesses if their number is higher or lower than the computer's."""

import random

def high_low_game():
    """Run a high-low guessing game where the player guesses if their number is higher or lower than the computer's."""
    print("🎲 Welcome to the High-Low Game! 🎲")

    # Generate numbers for player and computer
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    # Show the user's number
    print(f"Your number is: {your_number}")

    # Ask for a guess
    guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()

    # Determine the result
    if guess == "higher":
        correct = your_number > computer_number
    elif guess == "lower":
        correct = your_number < computer_number
    else:
        print("Invalid input! Please type 'higher' or 'lower'.")
        return

    # Reveal computer's number and result
    print(f"The computer's number was: {computer_number}")
    if correct:
        print("✅ You guessed right! You get a point.")
    else:
        print("❌ Oops! Your guess was incorrect.")

# Run the game
if __name__ == "__main__":
    high_low_game()
