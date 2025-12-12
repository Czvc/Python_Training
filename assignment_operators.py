# Assignment operators are used to assign values to variables:
a = 20         
print("This is for equals assignment")
print(a)

# Addition assignment
b = 10
b += 3
print("This is for addition assignment")
print(b)

# Subtraction assignment
c = 15
c -= 5
print("This is for subtraction assignment")
print(c)

# Multiplication assignment
d = 4
d *= 2
print("This is for multiplication assignment")
print(d)

# Division assignment
e = 20
e /= 4
print("This is for division assignment")
print(e)

# Modulus assignment
f = 10
f %= 3
print("This is for modulus assignment")
print(f)

# Floor division assignment
g = 15
g //= 4
print("This is for floor division assignment")
print(g)

# Exponentiation assignment
h = 2
h **= 3
print("This is for exponentiation assignment")
print(h)

# Bitwise AND assignment
i = 5  # In binary: 0101
i &= 3  # In binary: 0011
print("This is for bitwise AND assignment")
print(i)

# Bitwise OR assignment
j = 5  # In binary: 0101
j |= 3  # In binary: 0011
print("This is for bitwise OR assignment")
print(j)

# Bitwise XOR assignment
k = 5  # In binary: 0101
k ^= 3  # In binary: 0011
print("This is for bitwise XOR assignment")
print(k)

# Bitwise right shift assignment
l = 20  # In binary: 10100
l >>= 2
print("This is for bitwise right shift assignment")
print(l)

# Bitwise left shift assignment
m = 5  # In binary: 0101
m <<= 1
print("This is for bitwise left shift assignment")
print(m)    

# Walrus operator (assignment expression)
print("This is for walrus operator assignment")
print(x := 3)

# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
y = 10
if (z := y + 5) > 12:
    print("This is for walrus operator in conditional")
    print(z)

# Another example of walrus operator
print("This is another example of walrus operator")
cars = ["Toyota", "Honda", "Nissan", "Porsche", "Lexus"]
count = len(cars)
if count > 3:
    print(f"List has {count} elements")

if (count := len(cars)) > 3:
    print(f"List has {count} elements")

