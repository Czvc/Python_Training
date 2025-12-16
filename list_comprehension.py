# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
sports = ["basketball", "volleyball", "badminton", "football", "f1"]
newsports = [x for x in sports if "a" in x]
print("This is for list comprehension:")
print(newsports)

# List comprehension can also be used as a condition that only accepts the items that evaluate to True.
newlist = [x for x in sports if x != "badminton"]
print("This is list comprehension as a condition:")
print(newlist)

# List comprehension with the Iterable can be any iterable object, like a list, tuple, set etc.
numbers = [x for x in range(10) if x < 5]
print("This is for iteration:")
print(numbers)

# This is also a conditional list comprehension but with conditions
sports2 = [x if x != "football" else "swimming" for x in sports]
print("This is for list comprehension with conditions:")
print(sports2)