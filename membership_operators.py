# Membership operators are used to test if a sequence is presented in an object:
""" 'in' returns True if a sequence with the specified value is present in the object, 
while 'not in' returns True if a sequence with the specified value is not present in the object"""

# Check if Toyota is present and Check if Lexus is not present in the cars list
cars = ["Toyota", "Nissan", "Honda"]
check_car = "Toyota"
check_car2 = "Lexus"
if check_car in cars:
    print("Toyota is in the cars list")
if check_car2 not in cars:
    print("Lexus is not in the cars list")

# The membership operators also work with strings:
text = "Toyota Numbawan"

print("T" in text)
print("Toyota" in text)
print("Num" not in text)

