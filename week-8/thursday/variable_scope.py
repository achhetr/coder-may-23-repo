a = 10 # global scope


def print_a(): # function scope or block scope
    b = a
    b += 1
    print(a)

print_a()

print(a)
