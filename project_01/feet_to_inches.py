"""Module for converting feet to inches."""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    """Convert feet to inches and display the result."""
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    # Display the result
    unit = "foot" if feet == 1 else "feet"
    print(f"{feet} {unit} is equal to {inches} inches.")

if __name__ == '__main__':
    main()