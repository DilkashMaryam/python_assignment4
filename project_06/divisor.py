def print_divisors(num: int):
    """Prints all divisors of the given number."""
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    """Prompts the user for a number and prints all its divisors."""
    num = int(input("Enter a number: "))
    print_divisors(num)


if __name__ == '__main__':
    main()