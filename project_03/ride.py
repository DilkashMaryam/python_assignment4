"""Module which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height."""
MINIMUM_HEIGHT : int = 50 

def main():
    """Prompts user for height and determines if they meet the minimum height requirement."""
    height = float(input("How tall are you? "))
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


if __name__ == '__main__':
    main()