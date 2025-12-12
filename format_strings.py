# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 24
# message = "Happy " + age + "th Birthday!"
# This will raise a TypeError because we are trying to concatenate a string with an integer.

# But we can combine strings and numbers by using f-strings or the format() method!
# Using f-strings (available in Python 3.6 and later)
age = 24
message_fstring = f"Happy {age}th Birthday!"
print(message_fstring)

# A placeholder can contain variables, operations, functions, and modifiers to format the value.
# Using the format() method
message_format = "Happy {}th Birthday!".format(age)
print(message_format)

"""A placeholder can include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:"""
price = 49
message_price_fstring = f"The price is ${price:.2f}"
print(message_price_fstring)

# A placeholder can contain Python code, like math operations:
quantity = 3
total_fstring = f"Total price is ${price * quantity:.2f}"
print(total_fstring)
