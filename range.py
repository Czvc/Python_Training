""" The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
This set of numbers has its own data type called range."""

# Using range() with one argument
x = range(24)
print("range() with one argument:")
print(list(x))

# Using range() with two arguments
x2 = range(23, 35)
print("range() with two arguments:")
print(list(x2))

# Using range() with three arguments
x3 = range(23, 35, 1)
print("range() with three arguments:")
print(list(x3))

# Using range() in for loop
print("range() in for loop:")
for i in range(12):
  print(i)

# Using list to diplay ranges
print("using list to display range()")
print(list(range(6)))
print(list(range(1, 4)))
print(list(range(5, 25, 5)))

# Slicing ranges
r = range(10)
print("Slicing ranges:")
print(r[5])
print(r[:8])

# Testing range() using 'in'
r = range(0, 6, 3)
print("Test if the specified numbers is present in the range:")
print(3 in r)
print(7 in r)

# len() can also be used in a range 
r = range(0, 20, 2)
print("Using len() function to check the length of the range:")
print(len(r))

