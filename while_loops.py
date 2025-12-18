# while loops with and without break

i = 495
print("While loop test without break:")
while i <= 500:
  print(i)
  i += 1

i = 1
print("While loop with break:")
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue statement
i = 0
print("While loop with continue statement:")
while i < 6:
  i += 1
  if i == 4:
    continue
  print(i)

# else statement
i = 1
print("While loop with else statement:")
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")

