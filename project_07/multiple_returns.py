def get_user_info():
    """Get user information from input and return it as a tuple."""
    first_name: str = input("What is your first name?: ")
    last_name: str = input("What is your last name?: ")
    email_address : str = input("What is your email address?: ")
    
    return first_name, last_name, email_address


def main():
    """Main function that gets user info and prints it."""
    user_data = get_user_info()
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()