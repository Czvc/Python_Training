# There are several ways to join, or concatenate, two or more lists in Python.
# Use + operator
letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]
numters = letters + numbers
print("Join lists using '+' operator:")
print(numters)

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
for x in numbers:
    letters.append(x)
print("Join lists using append() method:")
print(letters)

# extend() method can also be used to join lists by adding elements from one list to another list
letters2 = ["f", "g", "h", "i", "j"]
numbers2 = [6, 7, 8, 9, 10]
letters2.extend(numbers2)
print("Join lists using extend() method:")
print(letters2)

