# Python If...Else
# Use if statements to compare values and run code only when a condition is True.

print("This is for basic if:")
country = "Philippines"

# Python If
# Simple condition: run the block if True.
if country == "Philippines":
    print("Mabuhay! You picked the right country.")

print("\nThis is for if with comparison:")
age = 18
if age >= 18:
    print("You can vote, at least in countries that remember elections.")

# Python Elif
print("\nThis is for if / elif / else:")
temperature = 35

if temperature > 40:
    print("Feels like the Sahara.")
elif temperature > 30:
    print("Feels like Manila at noon.")
else:
    print("Maybe you are in Baguio.")

# Python Else
print("\nThis is for if / else:")
country = "Japan"

if country == "Philippines":
    print("You get unlimited rice.")
else:
    print("No problem, other countries have good food too.")

# Shorthand If
print("\nThis is for shorthand if:")
score = 90
if score > 80: print("High score! Some countries would give you a parade.")

# Shorthand If...Else
print("\nThis is for shorthand if...else:")
country = "Canada"
message = "So cold but so polite." if country == "Canada" else "Weather unknown, check Google."
print(message)

# Logical Operators (and, or, not)
print("\nThis is for logical operators with countries:")
country = "Philippines"
continent = "Asia"

if country == "Philippines" and continent == "Asia":
    print("Correct, the map still works.")

if country == "Philippines" or country == "Spain":
    print("Either you love adobo or tapas, both are good choices.")

if not country == "Antarctica":
    print("Good news: your country actually has people.")

# Nested If
print("\nThis is for nested if:")
country = "Philippines"
city = "Cebu"

if country == "Philippines":
    print("Country is Philippines.")
    if city == "Cebu":
        print("You are in Cebu, enjoy the lechon!")
    else:
        print("Still in the Philippines, just a different city.")

# Pass Statement
print("\nThis is for pass statement:")
country = "Unknown"

if country == "Mars":
    # We are not ready to handle Martian citizenship yet.
    pass

print("Program continues even when we are confused about the country.")
