# List items are indexed and you can access them by referring to the index number:
brands = ["Samsung", "Apple", "OnePlus"]
print("This is for indexing:")
print(brands[1])

# Negative indexing means start from the end
cars = ["Toyota", "Nissan", "Mazda"]
print("This is for negative indexing:")
print(cars[-1])

# Range of indexes, You can specify a range of indexes by specifying where to start and where to end the range.
jdmcars = ["Toyota", "Nissan", "Mazda", "Subaru", "Suzuki", "Honda", "Lexus"]
print("Range of indexes:")
print(jdmcars[2:5])

# by leaving out the start value, the range will start at the first item
print("No start value:")
print(jdmcars[:3])    

# by leaving out end value, the range will go on to the end of the list
print("No end value:")
print(jdmcars[2:])      

# Range of negative index
print("Negative index:")
print(jdmcars[-4:-1])

# Check if item exist
if "Lexus" in jdmcars:
    print("Check if item exist:")
    print("'Lexus' is in the jdmcars list")