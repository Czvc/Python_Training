"""A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern."""

# to use RegEx, import re
import re

# sample txt
txt = "I love Nike shoes and Adidas shirts."

print("This is for search():")
m = re.search("Nike", txt)
print(m)

print("This is for findall():")
matches = re.findall("a", txt)
print(matches)

print("This is for findall() no match:")
print(re.findall("Puma", txt))

print("This is for search() span():")
m = re.search("Adidas", txt)
print(m.span())

print("This is for search() start and end word:")
print(m.start())
print(m.end())

print("This is for search() group():")
print(m.group())

# Meta characters
print("This is for . (any character):")
print(re.findall("N.ke", txt))

print("This is for ^ (starts with):")
print(bool(re.search("^I love", txt)))

print("This is for $ (ends with):")
print(bool(re.search(r"shirts\.$", txt)))

print("This is for * (zero or more):")
print(re.findall("Ni*ke", "Niiiiike Nike Nke"))

print("This is for + (one or more):")
print(re.findall("Ni+ke", "Nike Niiike Nke"))

print("This is for ? (zero or one):")
print(re.findall("colou?r", "color colour colouur"))

print("This is for {} (exact count):")
print(re.findall("o{2}", "Soo cool in a room"))

print("This is for [] (character set):")
print(re.findall("[ns]", txt))

print("This is for | (or):")
print(re.findall("Nike|Puma", txt))

# Sets examples
print("This is for [a-m]:")
print(re.findall("[a-m]", txt))

print("This is for [^a-m] (not a-m):")
print(re.findall("[^a-m]", "abcXYZ123"))

print("This is for [0-9]:")
print(re.findall("[0-9]", "My order number is 12345"))

print("This is for [a-zA-Z]:")
print(re.findall("[a-zA-Z]", "Nike2024!"))

# Special sequences
sample = "Order 123 from shop 7"

print("This is for \\d (digits):")
print(re.findall(r"\d", sample))

print("This is for \\D (non-digits):")
print(re.findall(r"\D", sample))

print("This is for \\s (whitespace):")
print(re.findall(r"\s", sample))

print("This is for \\S (non-whitespace):")
print(re.findall(r"\S", sample))

print("This is for \\w (word characters):")
print(re.findall(r"\w", sample))

print("This is for \\W (non-word characters):")
print(re.findall(r"\W", "Nike-2024!"))

print("This is for \\b (word boundary):")
print(re.findall(r"\bshop", sample))

print("This is for \\B (no word boundary):")
print(re.findall(r"\Bop", "shopstop"))

# split()
print("This is for split():")
print(re.split(r"\s", txt))

print("This is for split() with maxsplit=2:")
print(re.split(r"\s", txt, 2))

# sub()
print("This is for sub():")
print(re.sub("Nike", "Puma", txt))

print("This is for sub() with count=1:")
print(re.sub("a", "*", txt, 1))

# Match object example
print("This is for Match object info:")
m = re.search(r"N\w+", txt)
print(m)
print(m.span())
print(m.string)
print(m.group())