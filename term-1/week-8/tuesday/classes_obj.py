# a student with attributes like name, age, and major

class Student:
    def __init__(self, name, age, major): # constructor
        self.name = name
        self.age = age
        self.major = major

marcus = Student("marcus", 21, "maths")
saul = Student("saul", 23, "python")

# class
# attributes
# constructors
# instance <-> object

# car = {
#     "color": "red",
#     "engine_size": 2.4,
#     "passenger": 4,
#     "fuel_type": "petrol"
# }

class Car:
    def __init__(self, color, engine_size, passenger, fuel_type):
        self.color = color
        self.fuel_type = fuel_type
        self.passenger = passenger
        self.engine_size = engine_size

    def drives(self, direction):
        print(f"{self.color} is moving {direction} with {self.passenger} seat")


akash = Car("red", 2.4, 4, "petrol")
marcus = Car("blue", 2.8, 2, "electric")


akash.drives('forward')
marcus.drives('reverse')
