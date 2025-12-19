# Python has a built-in package called json, which can be used to work with JSON data.
import json

# If you have a JSON string, you can parse it by using the json.loads() method.
json_text = '{"brand": "Toyota", "model": "Ativ HEV", "year": 2025}'
car = json.loads(json_text)
print("json.loads() method:")
print(car)

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
person = {
    "name": "Chase",
    "age": 24,
    "city": "Caloocan"
}
json_data = json.dumps(person)
print("\njson.dumps() method:")
print(json_data)

# Convert Python objects into JSON strings, and print the values:
print("\nconvert python objects into JSON strings:")
print(json.dumps({"brand": "Toyota", "electric": False, "year": 2024}))
print(json.dumps(["Nike", "Adidas", "Puma"]))
print(json.dumps(("red", "green", "blue")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(3.14))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""You can also define the separators, default value is (", ", ": "), 
which means using a comma and a space to separate each object, and a colon and a space to separate keys from values"""
product = {
    "name": "T‑shirt",
    "brand": "Uniqlo",
    "sizes": ["S", "M", "L"],
    "price": 599
}
# with sort_keys parameter
print(json.dumps(product, indent=4, separators=(", ", " = "), sort_keys=True))
