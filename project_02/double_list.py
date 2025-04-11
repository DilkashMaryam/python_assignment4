def main():
    """
    Doubles each element in a list of numbers and prints the result.
    """
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i, elem in enumerate(numbers):  # Loop through the list with indices
        numbers[i] = elem * 2  # Double each element

    print(numbers)  # This should print the doubled list


if __name__ == '__main__':
    main()