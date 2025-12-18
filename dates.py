import datetime
# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

# checking the current date
x = datetime.datetime.now()
print("Today is", x)

# return the year and name of weekday using datetime()
print("Today is", x.strftime("%A"))

"""create a date using datetime() class from the datetime() module
the datetime() class requires three parameters to create a date: year, month, day"""
x = datetime.datetime(2025, 12, 25)
print("Christmas is on", x)
print("Christmas season starts on", x.strftime("%B"))
