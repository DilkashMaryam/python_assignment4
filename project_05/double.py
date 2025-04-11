"""Module that asks the user for a number, then keeps doubling it and printing the result until it is 100 or more:
python
Copy
Edit
"""

# Ask user to enter a number
curr_value = int(input("Enter a number: "))

# Keep doubling until the value is 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=' ')