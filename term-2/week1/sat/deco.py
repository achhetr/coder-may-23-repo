# simple decorator
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure

from functools import wraps

admin = False
def give_access(func):
    @wraps(func)
    def wrapper():
        if admin:
            func()
        else:
            print("Access denied")
    return wrapper

@give_access
def wifi_password():
    print("your home password `hero`")


print(wifi_password())
print(wifi_password)
