"""You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string."""

b = "Hello, Ortigas!"
print(b[0:5])  # Returns characters from index 0 to 4
# Note: The character at the end index is not included

# Omitting the start index will start the slice from the beginning of the string
print(b[:5])   # Returns characters from the beginning to index 4
# Omitting the end index will slice to the end of the string
print(b[7:])   # Returns characters from index 7 to the end
# You can also use negative indexing to slice from the end of the string
print(b[-8:-1])  # Returns characters from index -8 to -2