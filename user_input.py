import math

# Python allows to ask users for input
name = input("Enter your name:")
age = input("Enter your age:")

print(f"Your Name is {name} and You are {age} years old")

# You can also convert the user input into a number with validation
y = True
while y == True:
   x = input("\nEnter a number:")
   try:
     x = float(x);
     y = False
   except:
     print("Wrong input, please input numbers only.")

# find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")
