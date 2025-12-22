# Python Classes and Objects 

# Create a Class 
class GamingLaptop:
    brand = "ASUS ROG"   # class property
    price = 150000       # another property

# Create Object from the Class 
laptop1 = GamingLaptop()

# Use the Object's Properties 
print(laptop1.brand)
print(laptop1.price)

# Create More Objects from the Same Class 
laptop2 = GamingLaptop()
laptop3 = GamingLaptop()

print(laptop2.brand)
print(laptop3.price)

# Delete an Object 
del laptop3

# Use pass in an Empty Class
class BackupLaptop:
    pass
