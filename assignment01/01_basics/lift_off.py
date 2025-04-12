"""A countdown program that prints numbers from 10 to 1 followed by 'Liftoff!'."""

def main():
    """Print a countdown from 10 to 1 and display 'Liftoff!'."""
    for i in range(10, 0, -1):
        print(i, end=" ")
    print("Liftoff!")

if __name__ == "__main__":
    main()