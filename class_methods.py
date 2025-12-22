# Python Class Methods
# Class methods are functions inside a class that define what its objects can do.

print("This is for a basic method in a class:")

class ToyotaSportsCar:
    def __init__(self, model, year):
        self.brand = "Toyota"
        self.model = model
        self.year = year

    def describe(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = ToyotaSportsCar("Supra", 2024)
car1.describe()

print("\nThis is for a method with parameters:")

class SpeedCalculator:
    def top_speed(self, base_speed, turbo_bonus):
        return base_speed + turbo_bonus

    def quarter_mile_time(self, seconds, driver_bonus):
        return seconds - driver_bonus

calc = SpeedCalculator()
print(calc.top_speed(250, 20))          # 250 km/h + 20 km/h bonus
print(calc.quarter_mile_time(12, 0.5))  # 12s - 0.5s

print("\nThis is for methods accessing properties with self:")

class TrackCar:
    def __init__(self, model, horsepower):
        self.brand = "Toyota"
        self.model = model
        self.horsepower = horsepower

    def get_info(self):
        return f"{self.brand} {self.model} with {self.horsepower} HP"

tc1 = TrackCar("GR Supra", 382)
print(tc1.get_info())

print("\nThis is for methods modifying properties:")

class TunedCar:
    def __init__(self, model, horsepower):
        self.brand = "Toyota"
        self.model = model
        self.horsepower = horsepower

    def add_tune(self, extra_hp):
        self.horsepower += extra_hp
        print(f"Tuned! {self.model} now has {self.horsepower} HP")

t1 = TunedCar("GR86", 228)
t1.add_tune(30)
t1.add_tune(20)

print("\nThis is for the __str__() method:")

class ShowCar:
    def __init__(self, model, color):
        self.brand = "Toyota"
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"

sc1 = ShowCar("Supra", "red")
print(sc1)   # calls __str__ automatically

print("\nThis is for multiple methods in one class:")

class Garage:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, model):
        self.cars.append(model)
        print(f"Added: {model}")

    def remove_car(self, model):
        if model in self.cars:
            self.cars.remove(model)
            print(f"Removed: {model}")

    def show_cars(self):
        print(f"Garage '{self.name}' Toyota sports cars:")
        for model in self.cars:
            print("-", model)

my_garage = Garage("Weekend Toys")
my_garage.add_car("Supra")
my_garage.add_car("GR86")
my_garage.show_cars()

print("\nThis is for deleting a method from a class (example only):")

class DemoCar:
    def honk(self):
        print("Beep beep!")

d1 = DemoCar()
d1.honk()

del DemoCar.honk
# d1.honk()  # would cause an error if uncommented
