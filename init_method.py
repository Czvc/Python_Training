print("This is for the __init__() method:")

# Class with __init__() that sets properties when the object is created.
class GamingLaptop:
    def __init__(self, brand, price):
        self.brand = brand      
        self.price = price      

laptop1 = GamingLaptop("ASUS ROG", 1500)
print(laptop1.brand)
print(laptop1.price)

print("\nThis is for creating an object WITHOUT __init__() (manual setup):")

# Why __init__() is useful: compare with a class that has no __init__().
class SimpleLaptop:
    pass

manual = SimpleLaptop()
manual.brand = "MSI"
manual.price = 1400

print(manual.brand)
print(manual.price)

print("\nThis is for using __init__() again to set values automatically:")

# Using __init__() again makes object creation shorter and safer.
class AutoLaptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

auto1 = AutoLaptop("Lenovo Legion", 1300)
print(auto1.brand)
print(auto1.price)

print("\nThis is for default values in __init__():")

# Default value in __init__() (price has a default).
class DefaultLaptop:
    def __init__(self, brand, price=1200):
        self.brand = brand
        self.price = price

dl1 = DefaultLaptop("Acer Predator")          # uses default price
dl2 = DefaultLaptop("Dell Alienware", 2000)   # custom price

print(dl1.brand, dl1.price)
print(dl2.brand, dl2.price)

print("\nThis is for __init__() with multiple parameters:")

# __init__() with more properties.
class FullLaptop:
    def __init__(self, brand, price, gpu, ram):
        self.brand = brand
        self.price = price
        self.gpu = gpu
        self.ram = ram

fl1 = FullLaptop("ASUS ROG", 1800, "RTX 4070", 16)

print(fl1.brand)
print(fl1.price)
print(fl1.gpu)
print(fl1.ram)
