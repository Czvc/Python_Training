"""To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert."""

"""An example of an illegal character is a double quote inside a string that is surrounded by double quotes:"""
# Using escape character to insert double quotes inside a string
message_with_quotes = "He said, \"Hello, how are you? I am under the water\""
print(message_with_quotes)

"""Without the escape character, 
the interpreter would think that the string ends at the first double quote after He said, causing a syntax error."""
# Example without escape character (will raise SyntaxError)
# message_with_quotes_error = "He said, "Hello, how are you? I am under the water""
# print(message_with_quotes_error)

# Here are some other escape characters you can use in Python strings:
# Single Quote: \'
single_quote_example = 'It\'s a beautiful day!'
print(single_quote_example)

# Backslash: \\
backslash_example = "This is a backslash: \\"
print(backslash_example)

# New Line: \n
new_line_example = "Hello,\nWelcome to the world of Python!"
print(new_line_example)

# Carriage Return: \r
carriage_return_example = "Hello, World!\rPython"
print(carriage_return_example)

# Tab: \t
tab_example = "Name:\tJohn Doe"
print(tab_example)

# Backspace: \b
backspace_example = "Hello, Worl\bld!"
print(backspace_example)

# Form Feed: \f
form_feed_example = "Hello,\fWorld!"
print(form_feed_example)

# Octal Value: \ooo
octal_example = "Character with octal value 101: \101"
print(octal_example)

# Hex Value: \xhh
hex_example = "Character with hex value 41: \x41"
print(hex_example)
