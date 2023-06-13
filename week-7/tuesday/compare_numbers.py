# find out maximum numbers out 3 numbers

# function to find the maximum number
def maximum(n1, n2, n3):
    # if checks
    # check if the first is greater and second and third
    if (n1 > n2 and n1 > n3):
        return n1

    if (n2 > n3 and n2 > n1):
        return n2

    if (n3 > n2 and n3 > n1):
        return n3

    return n3

# get 3 numbers from the user
n1 = int(input("Enter first number> "))
n2 = int(input("Enter second number> "))
n3 = int(input("Enter third number> "))


# compare 3 numbers to find out the max number
max_number = maximum(n1, n2, n3)

# display the maximum number
print(f"Max number is {max_number}")
