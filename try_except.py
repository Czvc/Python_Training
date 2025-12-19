# Basic try/except
try:
    print(car_brand)      # car_brand is not defined
except:
    print("An error happened!")

# Many exceptions
try:
    print(car_brand)      # NameError
except NameError:
    print("car_brand is not defined")
except:
    print("Some other error happened")

# Else runs when no error happens
try:
    car_brand = "Toyota"
    print(car_brand)
except:
    print("Something went wrong")
else:
    print("Everything worked fine")

# Finally always runs
try:
    print(car_brand)
except:
    print("Something went wrong")
finally:
    print("This message is shown no matter what")

# Using finally to close a file
try:
    f = open("brands.txt", "w")
    f.write("Toyota, Ford, BMW")
except:
    print("Problem opening or writing to the file")
finally:
    f.close()
    print("File closed")

# Raise your own exception
# Uncomment the code below to see the error:
""" 
speed = -5
if speed < 0:
    raise Exception("Speed cannot be negative")
"""

# Raise a TypeError if value is not an int
# Uncomment the code below to see the error:
"""
items = "ten"
if not isinstance(items, int):
    raise TypeError("items must be an integer")
"""
