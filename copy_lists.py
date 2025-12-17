# To copy a list you can use the built-in List method copy()
letters = ["a", "b", "c", "d", "e"]
mylist = letters.copy()
print("Copy a list using copy() method:")
print(mylist)

# Use built-in method list() to make a copy
mylist2 = list(letters)
print("Copy a list using list() method:")
print(mylist2)

# You can also make a copy of a list by using the : (slice) operator.
mylist3 = letters[:]
print("Copy a list using the ':' (slice operator):")
print(mylist3)