"""Module for demonstrating list operations with data copying."""

def add_three_copies(my_list, data):
    """Add three copies of the given data to the list."""
    for i in range(3):
        my_list.append(data)


def main():
    """Main function that prompts for input and demonstrates list modification."""
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()