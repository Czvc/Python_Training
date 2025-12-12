"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
'hello' is the same as "hello".
"""

# you can display a string literal with the print() function:
print("Hello")
print('Hello')

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's a beautiful day")
print('She said "Hello"')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Graduate" 
print(a)  # Output: Graduate

# You can use triple double quotes and also three single quotes for multi-line strings:
b = """This is a multi-line string.
It can span multiple lines.
"""
c = '''This is another multi-line string.
It also can span multiple lines.'''

print(b)
print(c)

"""Like many other popular programming languages, strings in Python are arrays of unicode characters.
However, Python does not have a character data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string."""
print()
print("This part is about string indexing:")
d = "Graduate"
print(d[0])  # Output: G
print(d[3])  # Output: d 

# Looping through a string
print()
print("Looping through the string:")
for char in d:
    print(char)

# String length
print()
print("String length:")
print(len(d))  # Output: 8

# To check if a certain phrase or character is present in a string, we can use the keyword in.
print()
print("Checking for substring presence:")
phrase = "Graduate"
print("Is 'du' present in Graduate? ", "du" in phrase)  # Output: True
print("Is 'cat' present in Graduate? ", "cat" in phrase)  # Output: False
print("Is 'cat' not present in Graduate? ", "cat" not in phrase)  # Output: True

# Use it in an if statement:
print()
if "du" in phrase:
    print("Yes, 'du' is present in the phrase.")
if "cat" not in phrase:
    print("No, 'cat' is not present in the phrase.")



