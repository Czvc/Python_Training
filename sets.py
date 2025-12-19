# Python Sets
# A set is an unordered collection of unique items (no duplicates).
print("This is for creating sets:")
brands = {"Toyota", "Honda", "Ford"}
print(brands)

# Access Set Items
# You cannot use indexes, but you can loop and check membership with "in".
print("This is for accessing set items:")
print("Toyota" in brands)
print("BMW" in brands)

# Add Set Items
# add() adds a single car brand to the set.
print("This is for add():")
brands.add("BMW")
print(brands)

# update() adds multiple car brands from another collection.
print("This is for update():")
more_brands = ["Nissan", "Mazda"]
brands.update(more_brands)
print(brands)

# Remove Set Items
# remove() deletes a brand and raises an error if it does not exist.
print("This is for remove():")
brands.remove("Ford")
print(brands)

# discard() deletes a brand but does nothing if it does not exist.
print("This is for discard():")
brands.discard("Ford")
print(brands)

# pop() removes and returns a random brand.
print("This is for pop():")
removed = brands.pop()
print("Removed:", removed)
print(brands)

# clear() empties the set.
print("This is for clear():")
brands.clear()
print(brands)

# Loop Sets
# Use a for-loop to go through all car brands in a set.
print("This is for looping sets:")
japanese = {"Toyota", "Honda", "Nissan"}
for brand in japanese:
    print(brand)

# Join Sets
set_a = {"Toyota", "Honda", "Ford"}
set_b = {"Ford", "BMW", "Audi"}

# union() creates a new set with brands from both sets.
print("This is for union():")
union_set = set_a.union(set_b)
print(union_set)

# update() adds brands from one set into another.
print("This is for update() with sets:")
set_a_copy = set_a.copy()
set_a_copy.update(set_b)
print(set_a_copy)

# Frozenset
# A frozenset is like a set, but the brands cannot be changed.
print("This is for frozenset:")
european = frozenset({"BMW", "Audi", "Mercedes"})
print(european)

# Set Methods
# intersection, difference, symmetric_difference, subset/superset, etc.
print("This is for intersection():")
print(set_a.intersection(set_b))      # brands in both sets

print("This is for difference():")
print(set_a.difference(set_b))        # in set_a but not in set_b

print("This is for symmetric_difference():")
print(set_a.symmetric_difference(set_b))  # in one set but not both

print("This is for issubset() and issuperset():")
small = {"Toyota", "Honda"}
big = {"Toyota", "Honda", "Nissan", "Mazda"}
print(small.issubset(big))
print(big.issuperset(small))

print("This is for isdisjoint():")
print(small.isdisjoint({"BMW", "Audi"}))
