"""Module that contains list of fruits"""

def main():
    """Create and manipulate a list of fruits, demonstrating basic list operations."""
    #create a list called fruit_list that contain following fruits:
    fruit_list = ['apple','banana','orange','grape','pineapple']

    #print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    print("Updated fruit list:", fruit_list)

# Call the main function
if __name__ == "__main__":
    main()