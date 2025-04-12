def access_element(lst, index):
    """Access and return an element from a list at the specified index."""
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Error: Index is out of range."

def modify_element(lst, index, new_value):
    """Modify an element in a list at the specified index with a new value."""
    try:
        old_value = lst[index]
        lst[index] = new_value
        return f"Element at index {index} changed from {old_value} to {new_value}."
    except IndexError:
        return "Error: Index is out of range."

def slice_list(lst, start, end):
    """Return a slice of the list from start index to end index."""
    if start < 0 or end > len(lst) or start >= end:
        return "Error: Invalid slice range."
    return lst[start:end]

def main():
    """Run the list manipulation game with user interaction."""
    # Initial list
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Welcome to the List Manipulation Game!")
    print("Initial list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            try:
                index = int(input("Enter the index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Please enter a valid integer for index.")

        elif choice == '2':
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value))
                print("Updated list:", my_list)
            except ValueError:
                print("Please enter a valid integer for index.")

        elif choice == '3':
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print("Sliced list:", result if isinstance(result, list) else result)
            except ValueError:
                print("Please enter valid integers for slicing.")

        elif choice == '4':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()
