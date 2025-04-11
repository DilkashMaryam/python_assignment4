#Ask the user for a number and print its square (the product of the number times itself).

#Here's a sample run of the program (user input is in bold italics):

#Type a number to see its square: 4

#4.0 squared is 16.0

def main():
    """Program that prompts the user for a number and prints its square (the product of the number times itself)."""
    number : float = float(input("Type a number to see its square: "))
    print(str(number) + " squared is " + str(number ** 2))

if __name__ == "__main__":
    main()