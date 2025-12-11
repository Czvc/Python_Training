"""
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""

# Example of casting to int
x = int(1)         # x will be 1
y = int(2.8)       # y will be 2
z = int("3")      # z will be 3
print(x)
print(y)
print(z)

# Example of casting to float
a = float(1)      # a will be 1.0
b = float(2.8)    # b will be 2.8
c = float("3")    # c will be 3.0
print(a)
print(b)
print(c)

# Example of casting to str
m = str(1)        # m will be '1'
n = str(2.8)      # n will be '2.8'
o = str("3")      # o will be '3'
print(m)
print(n)
print(o)