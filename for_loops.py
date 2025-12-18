# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
cars = ["Toyota", "Nissan", "Honda", "Mazda", "Lexus"]
print("Simple for loop example:")
for x in cars:
    print(cars)

print("Using for loop to loop through a string:")
for x in "Corolla":
    print(x)

print("For loop with break:")
for x in cars:
  print(x)
  if x == "Honda":
    break

print("For loop with break that comes before the print:")
for x in cars:
  if x == "Honda":
    break
  print(x)

# for loop with continue statement
print("For loop with continue statement:")
for x in cars:
  if x == "Nissan":
    continue
  print(x)

# for loop with range() function and else statement
print("For loop with range() and else statement:")
for x in range(10):
  print(x)
else:
  print("Doooooone!")

# the else block will not be executed if the loop is stopped by a break
print("For loop with range() and else statement stopped by break:")
for x in range(10):
  if x == 5: break
  print(x)
else:
  print("Doooooone!")

# nested for loops 
colors = ["black", "white", "red"]
cars2 = ["Porsche", "Lexus", "Lamborghini"]
print("Nested for loops:")
for x in colors:
  for y in cars2:
    print(x, y)

# pass statement
print("Testing the pass statement in for loop:")
for x in [4, 8, 12]:
  pass
