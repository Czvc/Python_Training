# Python Class Properties
# Class properties store data for each object and for the class itself.

print("This is for creating a class with properties:")

class ToyotaSportsCar:
    def __init__(self, model, year):
        # instance (object) properties
        self.brand = "Toyota"
        self.model = model
        self.year = year

car1 = ToyotaSportsCar("Supra", 2024)
print(car1.brand)
print(car1.model)
print(car1.year)

print("\nThis is for accessing properties with dot notation:")

print(car1.brand)   # object.property
print(car1.model)

print("\nThis is for modifying properties on an object:")

car1.year = 2025    # change property value
print(car1.year)

print("\nThis is for deleting a property from an object:")

del car1.year       # remove one property
print(car1.brand)   # still works
# print(car1.year)  # would give an error if uncommented

print("\nThis is for class properties vs object properties:")

class ToyotaSportsCar2:
    maker = "Toyota"   # class property (shared by all cars)

    def __init__(self, model):
        self.model = model   # instance property (per car)

ts1 = ToyotaSportsCar2("GR Supra")
ts2 = ToyotaSportsCar2("GR86")

print(ts1.model)
print(ts2.model)
print(ts1.maker)
print(ts2.maker)

print("\nThis is for modifying a class property (affects all objects):")

ToyotaSportsCar2.maker = "Toyota Gazoo Racing"

print(ts1.maker)
print(ts2.maker)

print("\nThis is for adding new properties to a single object:")

ts1.color = "red"
ts1.horsepower = 382

print(ts1.model)
print(ts1.color)
print(ts1.horsepower)
