# List objects have a sort() method that will sort the list alphanumerically and also numerically, ascending, by default:
letters = ["A", "B", "C", "D", "E"]
numbers = [100, 23, 34, 45, 50]
letters.sort()
numbers.sort()
print("This is the default for sort() method:")
print(letters)
print(numbers)

# Using reverse=True will sort the list in descending order
letters.sort(reverse=True)
numbers.sort(reverse=True)
print("This is sorted in descending order:")
print(letters)
print(numbers)

# You can also customize your own function by using the keyword argument key = function
def myfunc(n):
  return abs(n - 50)

numbers.sort(key = myfunc)
print("This is a customized function to sort the list:")
print(numbers)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
brands = ["abclothing", "H&M", "Zara", "uniqlo"]
brands.sort()
print("This is for testing if sort() is case sensitive:")
print(brands)
brands.sort(key = str.lower)
print(brands)

# If you want to reverse the order of the list regardless of the alphabet
brands.reverse()
print(brands)


