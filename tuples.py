# Python Tuples
# Tuples are like lists, but they cannot be changed (immutable).
print("This is for creating tuples:")
brands = ("Nike", "Adidas", "Puma")
print(brands)

# Access Tuples
# You can access items by index, negative index, or a range (slice).
print("This is for accessing tuples:")
print(brands[0])      # first item
print(brands[-1])     # last item
print(brands[1:3])    # items from index 1 up to (but not including) 3

# Update Tuples
# Tuples cannot be changed directly, so convert to list, edit, then convert back.
print("This is for updating tuples (via list):")
temp = list(brands)
temp[0] = "New Balance"
brands = tuple(temp)
print(brands)

# To add an item, create a new tuple and use + to join them.
print("This is for adding items (create new tuple):")
brands = brands + ("Under Armour",)
print(brands)

# To remove an item, change to list, remove it, then convert back to tuple.
print("This is for removing items (via list):")
temp = list(brands)
temp.remove("Puma")
brands = tuple(temp)
print(brands)

# Unpack Tuples
# Unpacking means splitting a tuple into separate variables.
print("This is for unpacking tuples:")
shoes = ("Nike", "Adidas", "Puma")
(a, b, c) = shoes
print(a)
print(b)
print(c)

# The * operator in unpacking collects extra items into a list.
print("This is for unpacking with *:")
shoes = ("Nike", "Adidas", "Puma", "New Balance", "Reebok")
(first, *middle, last) = shoes
print(first)
print(middle)
print(last)

# Loop Tuples
# You can loop over a tuple directly with a for loop.
print("This is for looping tuples (for):")
for b in brands:
    print(b)

# You can also loop using indexes with range(len()).
print("This is for looping tuples (index):")
for i in range(len(brands)):
    print(i, brands[i])

# A while loop works too by increasing an index manually.
print("This is for looping tuples (while):")
i = 0
while i < len(brands):
    print(brands[i])
    i += 1

# Join Tuples
# Use + to join two tuples into a new, bigger tuple.
print("This is for joining tuples:")
more_brands = ("Fila", "Sketchers")
all_brands = brands + more_brands
print(all_brands)

# Multiplying a tuple repeats its contents.
print("This is for multiplying tuples:")
triple = ("Nike",) * 3
print(triple)

# Tuple Methods (count and index)
# count() tells how many times a value appears; index() gives the first position.
print("This is for tuple methods (count and index):")
nums = (1, 2, 2, 3, 2)
print(nums.count(2))
print(nums.index(3))
