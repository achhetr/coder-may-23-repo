# single responsibility principles of a function
# problem: Number Guessing

from random import randint

def generates_random_number():
    """random number between 1 to 50"""
    return randint(1, 50)

def get_user_input():
    try:
        user_input = int(input("Enter your guess(numbers only)> "))
    except ValueError:
        return 1
    else:
        return user_input

# program generates a number to guess between 1 to 50
random_number = generates_random_number()

# user inputs a number
user_input = get_user_input()

# based on the output we give hints

# win or retry

# send total retires
