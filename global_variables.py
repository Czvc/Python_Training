"""Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside."""
x = "GR GT"

def myfunc():
  print("Toyota revealed the new " + x)
myfunc()

"""If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value."""

# Create a variable inside a function, with the same name as the global variable
x = "GR GT"
def myfunc():
  x = "LFA Concept"
  print("Lexus revealed the new " + x)
myfunc()

# If you use the global keyword, the variable belongs to the global scope:
x = "GR GT"
def myfunc():
  global x
  x = "LFA Concept"
myfunc()

print("Lexus revealed the new " + x)

"""Also, use the global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, refer to the variable by using the global keyword:"""
x = "Civic Type R"
def myfunc():
  global x
  x = "Prelude"
myfunc()
print("Honda released the new " + x)