from string import ascii_letters, digits
from random import choice
from re import search
# password generator
# to create a strong password
# length of the password
# uppercase lowercase string.ascii_letters
# numbers string.digits
# symbols (_, .)

# get length of the password as an input from the user
def get_password_length_from_user():
    password_length = int(input("Enter password length> "))

    while password_length <= 6:
        password_length = int(input(f"Enter new password length as previous length was {password_length}> "))

    return password_length

def password_combination(password_length):
    # constant containing valid password characters
    valid_characters = ascii_letters + digits + "_."

    # create a variable to save password
    password = ""

    # iterate on the length of the password to get random character
    for i in range(password_length):
        password += choice(valid_characters)

    return password

def valid_password(password):
    if not password:
        return False

    # using regular expression
    # has_uppercase = bool(search(r'[A-Z]', password))
    # has_lowercase = bool(search(r'[a-z]', password))
    # has_digit = bool(search(r'[0-9]', password))
    # has_punctuations = bool(search(r'[_|.]', password))
    has_upper = False
    has_lower = False
    has_digit = False
    has_punc = False

    for c in password: #AAAAAAAAAAAAAccccccccc9_
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c == "_" or c == ".":
            has_punc = True

        if has_upper and has_lower and has_digit and has_punc:
            return True

    return False

def generate_password():
    password_length = get_password_length_from_user()
    while True:
        gen = password_combination(password_length)
        if valid_password(gen):
            return gen

# display password
print(generate_password())
