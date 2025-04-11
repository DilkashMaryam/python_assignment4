"""Module for determining if a person is an adult based on age."""

ADULT_AGE : int = 18 # U.S. age 

def is_adult(age: int):
    """Determine if a person is an adult based on age.
    
    Args:
        age: The age of the person
        
    Returns:
        True if the person is an adult, False otherwise
    """
    if age >= ADULT_AGE:
        return True
    
    return False


def main():
    """Main function that gets user input and prints whether the person is an adult."""
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()