# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(9, 18, 90, 1)
y = max(10, 20, 8, 100)
print("The minimum is", x, "while the maximum is", y)

negats = abs(-55.6)
print("Converted -55.6 to", negats)

power = pow(100, 2)
print("100 squared is equal to", power)

"""Python has also a built-in module called math, which extends the list of mathematical functions.
To use it we need to import math"""
import math

x = math.sqrt(999)
print("The square root of 999 is", x)

"""The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() 
method rounds a number downwards to its nearest integer, and returns the result:
"""
x = math.ceil(67.5)
y = math.floor(107.5)
print("67.5 is rounded up to", x, "while 107.5 is rounded down to", y)

# math.pi returns the value of Pi
x = math.pi
print("The value of Pi is", x)


