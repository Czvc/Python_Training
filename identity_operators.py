# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

""" 'is' returns True if both variables are the same object
'is not' returns True if both variablesare not the same object"""

cars_a = ["Toyota", "Nissan", "Honda"]
cars_b = ["Toyota", "Nissan", "Honda"]
cars_c = cars_a

print("This is for 'is' operator")
print(cars_a is cars_c) # True: same list object
print(cars_a is cars_b) # False: same values, different objects
print(cars_a == cars_b) # True: values are equal

# The is not operator returns True if both variables do not point to the same object:
brands_a = ["H&M", "Zara"]
brands_b = ["H&M", "Zara"]

print("This is for 'is not' operator ")
print(brands_a is not brands_b)

""" Difference of 'is' and '==', 'is' checks if both variables point to same object in memory, 
while '==' checks if both variables are equal"""

gadgets_a = ["Laptop", "PC", "Mobile Phone"]
gadgets_b = ["Laptop", "PC", "Mobile Phone"]

print("This is to show the difference of 'is' and '=='")
print(gadgets_a is gadgets_b)
print(gadgets_a == gadgets_b)






