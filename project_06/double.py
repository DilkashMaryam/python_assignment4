"""A simple module that doubles a given number."""

def double(num: int):
    """Doubles the given number and returns the result."""
    return num * 2

def main():
    """Prompts the user for a number and displays its double."""
    num = int(input("Enter a number: "))
    num_times_2 = double(num)
    print("Double that is", num_times_2)

if __name__ == '__main__':
    main()