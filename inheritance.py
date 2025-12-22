# Python Inheritance
# Inheritance lets a child class reuse and extend code from a parent class.

print("This is for creating a parent class:")

class HondaCar:
    def __init__(self, model, year):
        self.brand = "Honda"
        self.model = model
        self.year = year

    def show_name(self):
        print(self.year, self.brand, self.model)

parent_car = HondaCar("Civic", 2020)
parent_car.show_name()

print("\nThis is for creating a child class that inherits from the parent:")

class HondaSports(HondaCar):
    # child class inherits properties and methods from HondaCar
    pass

sports1 = HondaSports("Civic Type R", 2023)
sports1.show_name()   # uses method from parent class

print("\nThis is for adding __init__() in the child class (overrides parent):")

class HondaSports2(HondaCar):
    def __init__(self, model, year):
        # here we could add our own setup (but this would stop parent __init__ from running)
        self.brand = "Honda"
        self.model = model
        self.year = year

sports2 = HondaSports2("NSX", 2022)
sports2.show_name()

print("\nThis is for keeping parent __init__() using the parent name:")

class HondaSports3(HondaCar):
    def __init__(self, model, year):
        HondaCar.__init__(self, model, year)  # call parent __init__

sports3 = HondaSports3("Integra Type R", 2001)
sports3.show_name()

print("\nThis is for using super() to call the parent __init__():")

class HondaSports4(HondaCar):
    def __init__(self, model, year):
        super().__init__(model, year)  # super() calls HondaCar.__init__

sports4 = HondaSports4("S2000", 2009)
sports4.show_name()

print("\nThis is for adding new properties in the child class:")

class HondaStudentCar(HondaCar):
    def __init__(self, model, year, owner_name):
        super().__init__(model, year)
        self.owner_name = owner_name

    def welcome(self):
        print("Welcome", self.owner_name, "to your", self.year, self.brand, self.model)

student_car = HondaStudentCar("Civic Type R", 2024, "Chase")
student_car.welcome()

print("\nThis is for overriding a method in the child class:")

class LoudHonda(HondaCar):
    def show_name(self):
        # same name as parent method, but different behavior
        print("LOUD HONDA:", self.year, self.brand, self.model, "VTEC just kicked in!")

loud = LoudHonda("Civic Type R", 2025)
loud.show_name()
