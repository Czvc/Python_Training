# To change the value of a specific item, refer to the index number:
alcolist = ["Absolut", "Black Label", "Jack Daniel"]
alcolist[1] = "Hennessy"
print("Change a specific item from the list:")
print(alcolist)

# Change a range of item values
# Replace "Absolut" and "Jack Daniel" with two new cars
alcolist[1:3] = ["Lexus", "Mazda"]
print("Change a range of item values:")
print(alcolist)

# Replace three liquors with one car
alcolist[1:4] = ["Nissan GT-R"]
print(alcolist)   

# Insert items 
alcolist2 = ["Absolut", "Black Label", "Jack Daniel"]
alcolist2.insert(1, "Red Horse")
print("Insert new item:")
print(alcolist2)

