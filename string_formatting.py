# F-string allows you to format selected parts of a string.
price = 49
txt = f"The price is {price} dollars"
print(txt)

"""To format values in an f-string, add placeholders {}, 
a placeholder can contain variables, operations, functions, and modifiers to format the value."""
brand = "Toyota"
model = "Corolla"
txt = f"My car is a {brand} {model}"
print(txt)


"""A modifier is included by adding a colon : followed by a legal formatting type, 
like .2f which means fixed point number with 2 decimals:"""
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
txt = f"The price is {95:.2f} dollars"
print(txt)

# Operations in F-Strings
# simple math in the placeholder
txt = f"The total price is {20 * 59} pesos"
print(txt)

# add tax before showing price
price = 59
tax = 0.12
txt = f"The price with tax is {price + (price * tax)} pesos"
print(txt)

# conditional expression
price = 49
txt = f"This item is {'Expensive' if price > 50 else 'Affordable'}"
print(txt)

# You can execute functions inside the placeholder:
# using a built-in string method
brand = "nike"
txt = f"I like {brand.upper()} shoes"
print(txt)

# using your own function
def feet_to_meters(feet):
    return feet * 0.3048

distance = 10
txt = f"{distance} feet is {feet_to_meters(distance):.2f} meters"
print(txt)

# More modifiers
# thousand separator
price = 59000
txt = f"The price is {price:,} pesos"
print(txt)

# alignment examples
name = "Chase"
txt = f"|{name:<10}| left aligned"
print(txt)
txt = f"|{name:>10}| right aligned"
print(txt)
txt = f"|{name:^10}| centered"
print(txt)

# The format() method can still be used, but f-strings are faster and the preferred way to format strings.
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# If you want to use more values, just add more values to the format() method:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Also, if you want to refer to the same value more than once, use the index number:
age = 33
name = "Kyrie Irving"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

"""You can also use named indexes by entering a name inside the curly brackets {carname},
but then you must use names when you pass the parameter values"""
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Toyota", model="Supra"))


