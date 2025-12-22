# self lets each object access its own data and methods
print("This is for the self parameter and accessing properties:")

class GamingLaptop:
    def __init__(self, brand, price):
        # self refers to the current laptop object
        self.brand = brand
        self.price = price

    def show_info(self):
        # use self to read the properties of THIS object
        print("Brand:", self.brand)
        print("Price:", self.price)

l1 = GamingLaptop("ASUS ROG", 1500)
l1.show_info()

print("\nThis is for self linking each object to its own data:")

l2 = GamingLaptop("MSI", 1400)
l3 = GamingLaptop("Lenovo Legion", 1300)

l2.show_info()
l3.show_info()

print("\nThis is for self not needing to be named 'self' (but usually is):")

class LaptopAltName:
    def __init__(myobject, brand):
        myobject.brand = brand

    def greet(abc):
        print("This gaming laptop brand is", abc.brand)

la = LaptopAltName("Acer Predator")
la.greet()

print("\nThis is for self calling another method inside the class:")

class GamingLaptopFull:
    def __init__(self, brand, gpu):
        self.brand = brand
        self.gpu = gpu

    def short_specs(self):
        return self.brand + " with " + self.gpu

    def show_specs(self):
        # self calls another method of the same object
        text = self.short_specs()
        print(text)

gf = GamingLaptopFull("Dell Alienware", "RTX 4070")
gf.show_specs()
