# The remove() method removes the specified value.
cars = ["Toyota", "Nissan", "Mazda", "Honda", "Lexus"]
cars.remove("Honda")
print("This removes the specified value:")
print(cars)

# If there are more than one item of the specified value, the remove() method removes the first occurrence
liquor = ["Jack Daniel", "Bacardi", "Black Label", "Absolut", "Jack Daniel"]
liquor.remove("Jack Daniel")
print("This removes the first occurrence of the specified value:")
print(liquor)

# The pop() method removes the specified index
cars.pop(3)
print("This removes the specified index:")
print(cars)

# If you do not specify the index, the pop() method removes the last item.
liquor.pop()
print("This removes the last item if no index specified in pop() method:")
print(liquor)

# The del keyword also removes the specified index:
shoes = ["Nike", "Adidas", "Li Ning", "New Balance", "Jordan"]
del shoes[2]
print("This del() method also deletes the specified index:")
print(shoes)

# The del keyword can also delete the list completely.
del shoes
print("The del() method can also delete the list completely:")
# this "print(shoes)" will give an error 

# The clear() method empties the list.
hotel = ["Okada", "Manila Hotel", "Crimson Hotel Alabang"]
hotel.clear()
print("The clear() method will empty the list: ")
print("The list is empty:", hotel)
