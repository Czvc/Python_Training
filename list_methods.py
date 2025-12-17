# Python has a set of built-in methods that you can use on lists
"""
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
"""

cars = ["Toyota", "Ford"]
clothes = ["Nike", "Adidas", "Zara"]

# append() - adds item to end
print("This is for append():")
cars.append("Tesla")
print(cars)

# clear() - removes all items
print("This is for clear():")
clothes.clear()
print(clothes)

# copy() - creates shallow copy
print("This is for copy():")
backup_cars = cars.copy()
print(backup_cars)

# count() - returns occurrences
print("This is for count():")
brands = ["Nike", "Nike", "Adidas"]
print(brands.count("Nike"))

# extend() - adds multiple items
print("This is for extend():")
cars.extend(["BMW", "Honda"])
print(cars)

# index() - returns first index of value
print("This is for index():")
print(brands.index("Adidas"))

# insert() - adds item at index
print("This is for insert():")
cars.insert(1, "Audi")
print(cars)

# pop() - removes/returns last item (or at index)
print("This is for pop():")
last_car = cars.pop()
print(last_car)

# remove() - removes first occurrence
print("This is for remove():")
brands.remove("Nike")
print(brands)

# reverse() - reverses order in place
print("This is for reverse():")
cars.reverse()
print(cars)

# sort() - sorts in place (alphabetical for strings)
print("This is for sort():")
cars.sort()
print(cars)