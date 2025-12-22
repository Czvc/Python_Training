# Python Encapsulation
# Encapsulation hides internal details and controls how data is accessed or changed.

print("This is for a simple encapsulated class with Lexus cars:")

class LexusCar:
    def __init__(self, model, price):
        self.brand = "Lexus"      # public
        self.model = model        # public
        self._discount = 0.10     # protected (convention)
        self.__price = price      # private

    def get_price(self):
        # public method to read the hidden price
        return self.__price

    def set_price(self, new_price):
        # public method to safely change the price
        if new_price > 0:
            self.__price = new_price

lexus1 = LexusCar("LFA", 500000)
print(lexus1.brand, lexus1.model)
print("Price:", lexus1.get_price())

print("\nThis is for trying to change data directly vs using methods:")

# Direct public change (allowed)
lexus1.model = "LFA Nürburgring"
print("Updated model:", lexus1.model)

# Direct private change (this creates a new attribute, does not change real price)
lexus1.__price = 100
print("Wrong direct change (still old price inside):", lexus1.get_price())

# Correct change using the setter
lexus1.set_price(550000)
print("Updated price:", lexus1.get_price())

print("\nThis is for using a 'protected' attribute (single underscore):")

print("Discount (protected, but still readable):", lexus1._discount)

print("\nThis is for name mangling with private attributes:")

# Accessing the real private value through name mangling
print("Private price via name mangling:", lexus1._LexusCar__price)

print("\nThis is for encapsulation with a method that uses hidden data:")

class LexusDeal:
    def __init__(self, model, price):
        self.car = LexusCar(model, price)

    def final_price(self):
        # uses the internal car object and its hidden price and discount
        base = self.car.get_price()
        return base - (base * self.car._discount)

deal = LexusDeal("RC F", 80000)
print("Final price with discount:", deal.final_price())
