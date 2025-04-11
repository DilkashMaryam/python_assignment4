def main():
    """Main function that gets user input and prints a greeting."""
    name : str = input("What's your name? ")
    print(greet(name))


def greet(name):
    """Return a greeting message for the given name.
    
    Args:
        name: The name to greet
        
    Returns:
        A greeting string
    """
    return "Greetings " + name + "!"
	
if __name__ == '__main__':
    main()
