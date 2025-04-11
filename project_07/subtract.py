def main():
    """Main function that demonstrates subtracting seven from a number."""
    num: int = 7
    num = subtract_seven(num)
    print("this should be zero: ", num)

def subtract_seven(num):
    """Subtract seven from the given number.
    
    Args:
        num: The number to subtract from
        
    Returns:
        The result of subtracting seven
    """
    num = num - 7
    return num

if __name__ == '__main__':
    main()