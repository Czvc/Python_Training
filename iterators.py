# An iterator is an object that contains a countable number of values.

# using iterator in tuple, and string
cartuple = ["Toyota", "Nissan", "Honda"]
carit = iter(cartuple)
carstr = "Lexus"
strit = iter(carstr)

print("This example uses an iterator in tuple and string:")

print(next(carit))
print(next(carit))
print(next(carit))

print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))
print(next(strit))

# Using for loop to iterate through an iterable object
print("Iterate with for loop:")
for x in cartuple:
    print(x)

for x in carstr:
    print(x)

"""To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence."""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Create an Iterator
class BrandIterator:
    def __init__(self, brands):
        self.brands = brands      # the list we will iterate over
        self.index = 0            # start position

    def __iter__(self):
        return self              # the iterator object itself

    def __next__(self):
        if self.index < len(self.brands):
            item = self.brands[self.index]
            self.index += 1
            return item
        
brands = ["Nike", "Adidas", "Puma", "Zara"]

my_brands = BrandIterator(brands)

print("This are my own Iterators:")
print(next(my_brands))
print(next(my_brands))
print(next(my_brands))
print(next(my_brands))

# Stop Iteration
class LimitedBrandIterator:
    def __init__(self, brands, limit):
        self.brands = brands
        self.limit = limit
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.limit and self.index < len(self.brands):
            item = self.brands[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

brands = ["Nike", "Adidas", "Puma", "Zara", "Uniqlo"]

my_limited_brands = LimitedBrandIterator(brands, 3)

print("This is for Stop Iteration:")
for brand in my_limited_brands:
    print(brand)
