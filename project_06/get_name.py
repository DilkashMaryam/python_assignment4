def get_name():
    """Returns a fixed name string."""
    return "Sophia"

def main():
    """Displays a greeting with the name returned by get_name()."""
    name = get_name() # get_name() will return a string which we store to the 'name' variable here
    print("Howdy", name, "! 🤠")

if __name__ == '__main__':
    main()