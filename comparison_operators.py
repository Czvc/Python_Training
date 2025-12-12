# Comparison operators are used to compare two values:
x = 28
y = 1

# Equal to
print("This is for equal to operator:")
print(x == y)  

# Not equal to
print("This is for not equal to operator:")
print(x != y)  

# Greater than
print("This is for greater than operator:")
print(x > y)  

# Less than
print("This is for less than operator:")
print(x < y)  

# Greater than or equal to
print("This is for greater than or equal to operator:")
print(x >= y)
# Less than or equal to
print("This is for less than or equal to operator:")
print(x <= y)

# Python allows you to chain comparison operators:
a = 5
print("This is for chained comparison operators:")
print(1 < a < 10)  # True because 1 < 5 and 5 < 10
print(1 < a > 10)  # False because 5 is not greater than 10
print(1 < a <= 5)  # True because 1 < 5 and 5 <= 5
print(1 > a < 10)  # False because 1 is not greater than 5