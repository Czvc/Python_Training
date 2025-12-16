# You loop through a list by using a for loop
cars = ["Toyota", "Nissan", "Mazda", "Honda"]
print("This is a normal for loop:")
for x in cars:
    print(x)

"""You can also loop through the list items by referring to their index number.
Use the range() and len() functions to create a suitable iterable."""

# by referring to their index number you can print all items
brands = ["Uniqlo", "H&M", "Zara", "Ralph Lauren"]
print("This is a for loop using index:")
for i in range(len(brands)):
    print(brands[i])

# You can loop through the list items by using a while loop.
i = 0
print("This is a while loop:")
while i < len(brands):
    print(brands[i])
    i = i + 1

# looping using list comprehension, this method has the shortest syntax
print("This is a comprehension list looping:")
[print (x) for x in brands]

