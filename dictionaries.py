# Python Dictionaries
# A dictionary stores data in key:value pairs.
print("This is for creating a dictionary:")
food = {
    "name": "adobo",
    "type": "ulam",
    "origin": "Philippines",
    "price": 120
}
print(food)

print("\nThis is for accessing items:")
# Access Items
# Access values using keys or the get() method.
print(food["name"])
print(food.get("price"))

print("\nThis is for keys(), values(), items():")
# View keys, values, and items.
print(food.keys())
print(food.values())
print(food.items())

print("\nThis is for changing items:")
# Change Items
# Change the value of an existing key.
food["price"] = 150
print(food)

print("\nThis is for update() to change:")
# Use update() to change multiple values.
food.update({"type": "main dish", "served_with": "rice"})
print(food)

print("\nThis is for adding items:")
# Add Items
# Adding a new key:value pair is done by simple assignment.
food["spice_level"] = "mild"
print(food)

print("\nThis is for update() to add:")
# update() can also add new items.
food.update({"rating": 5})
print(food)

print("\nThis is for pop():")
# Remove Items
# pop() removes the item with the given key and returns its value.
removed = food.pop("rating")
print("Removed rating:", removed)
print(food)

print("\nThis is for popitem():")
# popitem() removes the last inserted item.
last = food.popitem()
print("Removed last item:", last)
print(food)

print("\nThis is for del on a key:")
# del removes a specific key (we add it back first so it exists).
food["spice_level"] = "mild"
del food["spice_level"]
print(food)

print("\nThis is for looping keys:")
# Loop Dictionaries
# Re-create a dictionary for looping examples.
food = {
    "name": "sinigang",
    "type": "soup",
    "origin": "Philippines",
    "price": 130
}
for key in food:
    print(key)

print("\nThis is for looping values:")
for value in food.values():
    print(value)

print("\nThis is for looping items:")
for key, value in food.items():
    print(key, "=", value)

print("\nThis is for copy():")
# Copy Dictionaries
# copy() makes a shallow copy of the dictionary.
food_copy = food.copy()
print(food_copy)

print("\nThis is for dict() copy:")
# dict() can also be used to copy.
food_copy2 = dict(food)
print(food_copy2)

print("\nThis is for nested dictionaries:")
# Nested Dictionaries
# A dictionary can contain other dictionaries.
menu = {
    "dish1": {
        "name": "adobo",
        "price": 120
    },
    "dish2": {
        "name": "sinigang",
        "price": 130
    },
    "dish3": {
        "name": "halo-halo",
        "price": 90
    }
}
print(menu)

print("\nThis is for accessing nested dictionary:")
print(menu["dish2"]["name"])
print(menu["dish3"]["price"])

print("\nThis is for setdefault():")
# Dictionary Methods
# Show some common methods like setdefault, fromkeys, and update again.
extras = {}
extras.setdefault("drink", "sago't gulaman")
print(extras)

print("\nThis is for fromkeys():")
keys = ("starter", "main", "dessert")
default_menu = dict.fromkeys(keys, "not decided")
print(default_menu)

print("\nThis is for update() on nested:")
menu["dish1"].update({"special": True})
print(menu["dish1"])
