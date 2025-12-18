"""None is a special constant in Python that represents the absence of a value.
Its data type is NoneType, and None is the only instance of a NoneType object."""

wala = None
print("This line should have", wala)
print("Type:",type(wala))

result = None
if result is None:
    print("Wala naman")
else:
    print("Meron na")

if result is not None:
    print("Wala naman")
else:
    print("Meron na")

print("True or False:",bool(None))

# a function without return statement returns None
def myfunc():
    x = 23

x = myfunc()
print("Any more questions class?",x)