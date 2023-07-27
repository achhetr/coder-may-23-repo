# print("Hello world" # syntax error
# print(hello) # NameError
# years = 42
# msg = "Akash is " + years + "old" # TypeError
# msg = f"Akash is {years} old"
# print(msg)
# fruits = ["apple", "orange", "kiwi"]
# print(fruits[6]) # IndexError

num = 20

try:
    user = int(input("enter your favourite number> "))
    print(num/user)
except ZeroDivisionError:
    print("You cannot enter zero")
except ValueError:
    print("You cannot enter non digit")
else:
    print("valid input by user")
finally:
    print("program terminated")
