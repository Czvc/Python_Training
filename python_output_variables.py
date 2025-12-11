# The print() function is often used to output variables.
name = "Alice"
age = 30
height = 5.5
print("Name:", name)
print("Age:", age)
print("Height:", height)

# In the print() function, you output multiple variables, separated by a comma:
city = "Tokyo"
country = "Japan"
print("City:", city, "Country:", country)

# You can also use the + operator to output multiple variables:
brand = "Toyota"
model = "GR Corolla"
print("Car:", brand + " " + model)

# For numbers, the + character works as a mathematical operator:
price = 1000
tax = 150
total = price + tax
print("Total Price:", total)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
quantity = 3
# Uncommenting the next line will raise a TypeError
# print("Quantity: " + quantity)

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
print("Quantity:", quantity)