# Python Polymorphism
# Polymorphism lets the same function or method name work in many forms.

print("This is for function polymorphism with len():")

text = "Hello Ortigas!"
mytuple = ("Civic", "Accord", "City")
garage = {
    "brand": "Honda",
    "models": 3,
    "type": "Sedan"
}

print(len(text))    # number of characters in a string
print(len(mytuple)) # number of items in a tuple
print(len(garage))  # number of key/value pairs in a dictionary

print("\nThis is for class polymorphism (different classes, same method name):")

class HondaCar:
    def __init__(self, model):
        self.brand = "Honda"
        self.model = model

    def move(self):
        print("Driiiiiive!")

class HondaBoat:
    def __init__(self, model):
        self.brand = "Honda"
        self.model = model

    def move(self):
        print("Langooooooy!")

class HondaPlane:
    def __init__(self, model):
        self.brand = "Honda"
        self.model = model

    def move(self):
        print("Lipaaaaaad!")

car1 = HondaCar("Civic")
boat1 = HondaBoat("Marine Jet")
plane1 = HondaPlane("Jet Plane")

for vehicle in (car1, boat1, plane1):
    vehicle.move()   # same method name, different behavior

print("\nThis is for inheritance polymorphism with a parent class:")

class HondaVehicle:
    def __init__(self, model):
        self.brand = "Honda"
        self.model = model

    def move(self):
        print("Drive!")

class HondaRoadCar(HondaVehicle):
    pass  # inherits move() without changes

class HondaSpeedBoat(HondaVehicle):
    def move(self):
        print("Langoy!")

class HondaJet(HondaVehicle):
    def move(self):
        print("Lipad!")

road = HondaRoadCar("Civic Type R")
boat = HondaSpeedBoat("Marine")
jet = HondaJet("Jet")

for v in (road, boat, jet):
    print(v.brand, v.model, end=" -> ")
    v.move()
