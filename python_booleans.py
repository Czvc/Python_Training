# Booleans represent one of two values: True or False.
print(28 > 9)
print(1 == 100)
print(68 < 100)

a = 21
b = 500

if b > a:
    print("b is greater than a")
else:
    print("a is greater than or equal to b")

# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("LeBron James"))
print(bool(23))

x = "Michael Jordan"
y = 23
print(bool(x))
print(bool(y))

"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""
print(bool(""))
print(bool(0))
print(bool(["Toyota", "Honda", "Nissan"]))

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class MyClass:
    def __len__(self):
        return 0
    
myobj = MyClass()
print("This is the boolean value of myobj:", bool(myobj))

# You can create functions that returns a Boolean Value:
def myFunction():
    return True
print("The value returned by myFunction is:", myFunction())

# You can execute code based on the Boolean answer of a function:
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
number = 10
if isEven(number):
    print(number, "is an even number")
else:
    print(number, "is an odd number")
print("The value returned by isEven(7) is:", isEven(7))

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
czar = 911
print(isinstance(czar, int))

