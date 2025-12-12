# To add an item to the end of the list, use the append() method:
cars = ["Toyota", "Nissan", "Honda"]
cars.append("Mazda")        # add one item at the end
print(cars)             

# To insert a list item at a specified index, use the insert() method.
cars = ["Toyota", "Honda", "Subaru"]
cars.insert(1, "Nissan")    # insert at index 1 (second position)
print(cars)                 # ['Toyota', 'Nissan', 'Honda', 'Subaru']

# To append elements from another list to the current list, use the extend() method.
jdm_cars = ["Toyota", "Nissan"]
euro_cars = ["BMW", "Audi"]
jdm_cars.extend(euro_cars)  # add each item from euro_cars
print(jdm_cars)            

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
cars = ["Toyota", "Nissan"]
# Add items from a tuple
more_cars = ("Honda", "Mazda")
cars.extend(more_cars)
# Add characters from a string
cars.extend("GT")           # adds 'G', 'T' as separate items
print(cars)


