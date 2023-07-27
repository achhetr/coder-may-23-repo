class DBConnectionError(Exception): ...


def validate(username, password):
    raise DBConnectionError("Your db cannot be connected")
    return username == "marcus" and password == "123"

username = input("Enter your username> ")
password = input("Enter your password> ")

try:
    print("your details", username, password, "are", validate(username, password))
except DBConnectionError as err:
    print("error>>>>>>", str(err))
