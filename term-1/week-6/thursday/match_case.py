# Determine the grade based on a student's score
lukas = 10
# ( <40, <60, <80, <90, <95, > 95)

match (lukas):
    case range(40):
        print("lucas failed!")
    case range(40, 60):
        print("lucas scored grade D")
    case range(60, 80):
        print("lucas scored grade C")
    case range(80, 90):
        print("lucas scored grade B")
    case range(90, 95):
        print("lucas scored grade A")
    case _:
        print("lucas scored grade A+")


# v = "cb"

# match(v):
#     case "a":
#         print("apple")
#     case "b":
#         print("banana")
#     case _:
#         print("kiwi")

