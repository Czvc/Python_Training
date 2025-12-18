# An array is a special variable, which can hold more than one value at a time.
cars = ["Toyota", "Nissan", "Lexus", "Honda"]

# accessing the elements of an array
x = cars[0]
print("Accessing an element of an array:")
print(x)

# Modify the value of an array item
cars[3] = "Mazda"
print("Modifying the value of an array item:")
print(cars)

# Using len() method to return the length of an array
x = len(cars)
print("The array has", x, "elements")

# Looping, adding, and removing array elements
for x in cars:
    print (x)

cars.append("Volkswagen")
print("VW have been added:", cars)
cars.pop(3)
print("Item no. 3 has been removed:", cars)
cars.remove("Volkswagen")
print("No more VW:", cars)

