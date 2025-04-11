#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

#Prompt the user to enter the first number.

#Read the input and convert it to an integer.

#Prompt the user to enter the second number.

#Read the input and convert it to an integer.

#Calculate the sum of the two numbers.

#Print the total sum with an appropriate message.

def main():
    """Program that takes two numbers as input and displays their sum."""
    print("This program adds two numbers together.")
    first_number : str = input("Enter the first number: ")
    first_number = int(first_number)
    second_number : str = input("Enter the second number: ")
    second_number = int(second_number)
    total : int = first_number + second_number
    print(f"The sum of {first_number} and {second_number} = " + str(total) + ".")

if __name__ == "__main__":
    main()