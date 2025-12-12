# Lists are used to store multiple items in a single variable.
mylist = ["Lenovo", "Asus", "Razer"]
print(mylist)

"""List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc."""

# Try ordered and indexed
colors = ["red", "green", "blue"]
print("Ordered and Indexed: ")
print(colors[0])   
print(colors[1])   
print(colors[2])   

# Try changeable
colors = ["red", "green", "blue"]
colors[1] = "yellow"      
print("Changeable: ")
print(colors)             
colors.append("purple")   
print(colors)             

# Try allow duplicate values
colors = ["red", "green", "red", "blue"]
print("Allow duplicate values: ")
print(colors)        
print(colors[0])    
print(colors[2])     

# Using List length
cars = ["Toyota", "Nissan", "Honda", "Porsche"]
print("List length:")
print(len(cars))          
print("Number of fruits:", len(cars))

# Using Data types for List item
garage = ["Toyota Supra", 1998, 3.0, True]
print("List item - data types:")
print(garage[0])    
print(garage[1])    
print(garage[2])    
print(garage[3])                

# Using list() constructor
# From a tuple of brands
japanese_brands = list(("Toyota", "Nissan", "Honda"))
print("From a tuple of brands:")
print(japanese_brands)   # ['Toyota', 'Nissan', 'Honda']

# From a string (brand name to letters)
brand = "Mazda"
letters = list(brand)
print("From a string (brand name to letters):")
print(letters)           # ['M', 'a', 'z', 'd', 'a']

# Copy an existing list
track_cars = ["Nissan GT-R", "Toyota GR Yaris"]
track_cars_copy = list(track_cars)
print("Copy an existing list:")
print(track_cars_copy)   # ['Nissan GT-R', 'Toyota GR Yaris']


