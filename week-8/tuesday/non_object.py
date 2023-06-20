# approach for car example

car = ["red", 2.4, 4, "petrol"] # [color, engine size, passenger, fuel type]

car = {
    "color": "red",
    "engine_size": 2.4,
    "passenger": 4,
    "fuel_type": "petrol"
}

def same_car(car_model):
    new_car = dict(car_model)
    del new_car["passenger"]
    return new_car

marcus_car = same_car(car)
marcus_car["color"] = 'blue'

print(marcus_car)
