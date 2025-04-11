#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

def main():
    """Program that prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius."""
    fahrenheit : str = input("Enter a temperature in Fahrenheit: ")
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5.0/9.0)
    print(f"The temperature in Celsius is {celsius}.C")

if __name__ == "__main__":
    main()