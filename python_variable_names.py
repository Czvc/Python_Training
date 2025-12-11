"""Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords."""

# Legal variable names
myvar = "John1"
my_var = "John2"
_my_var = "John3"
myVar = "John4"
MYVAR = "John5"
myvar2 = "John6"

# Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

"""
Camel Case
Each word, except the first, starts with a capital letter:
"""
myVariableName = "Zedrik"

"""
Pascal Case
Each word starts with a capital letter:
"""
MyVariableName = "Zedrik"

"""
Snake Case
Each word is separated by an underscore character:
"""
my_variable_name = "Zedrik"


