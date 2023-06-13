# find the largest number between two numbers

# get two numbers from users in n1 and n2
n1 = int(input("Enter first number> "))
n2 = int(input("Enter second number> "))

# compare n1 and n2 to find out which one is greater
# output the larget number

if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n1 == n2:
    print(f"Both numbers are equal {n1}")
else:
    print(f"{n1} is smaller than {n2}")
