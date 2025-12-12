"""
Three numeric types in Python are:
1. int - Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
2. float - Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
           Float can also be scientific numbers with an "e" to indicate the power of 10.
3. complex - Complex number type, represents numbers with a real and imaginary part.
"""

w = 5e3  # float
x = 1 #int
y = -4.0 #float
z = 6 +8j #complex

# to confirm what type of number a variable is, use the type() function:
print(type(w))
print(type(x))
print(type(y))
print(type(z))

# You can convert from one type to another with the int(), float(), and complex() methods:
# convert float to int
a = 3.5
b = int(a) 
print("Converted from float to int:", b)

# convert int to float
c = 7
d = float(c)
print("Converted from int to float:", d)

# convert int to complex
e = 2
f = complex(e)
print("Converted from int to complex:", f)

# convert float to complex
g = 4.2
h = complex(g)
print("Converted from float to complex:", h)

"""
Python does not have a random() function to make a random number,
but Python has a built-in module called random that can be used to make random numbers:
"""
# Import the random module, and display a random number from 1 to 9:
import random

print("Random number between 1 and 9:", random.randrange(1, 9))