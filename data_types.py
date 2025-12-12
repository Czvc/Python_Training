"""
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# Print the data type of the variable x:
z = 99
print(type(z))

# In Python, the data type is set when you assign a value to a variable:
a = "What data type am I?"   #str
b = 20	#int	
c = 20.5    #float	
d = 1j	#complex	
e = ["Toyota", "Nissan", "Honda"]	#list	
f = ("Toyota", "Nissan", "Honda")	#tuple	
g = range(6)	#range	
h = {"name" : "Chase", "age" : 24}	#dict	
i = {"Toyota", "Nissan", "Honda"}	#set	
j = frozenset({"Toyota", "Nissan", "Honda"})	#frozenset	
k = True	#bool	
l = b"Hello"	#bytes	
m = bytearray(5)	#bytearray	
n = memoryview(bytes(5))	#memoryview	
o = None	#NoneType

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n))
print(type(o))
print("End of first section\n")

# If you want to specify the data type, you can use the following constructor functions:
a = str("What data type am I?")	#str
b = int(20)	#int
c = float(20.5)	#float
d = complex(1j)	#complex
e = list(("Toyota", "Nissan", "Honda"))	#list
f = tuple(("Toyota", "Nissan", "Honda"))	#tuple
g = range(6)	#range
h = dict(name="Chase", age=24)	#dict
i = set(("Toyota", "Nissan", "Honda"))	#set
j = frozenset(("Toyota", "Nissan", "Honda"))	#frozens
k = bool(5)	#bool
l = bytes(5)	#bytes
m = bytearray(5)	#bytearray
n = memoryview(bytes(5))	#memoryview
o = None	#NoneType

#display a to o together with their data types:
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(g,type(g))
print(h,type(h))
print(i,type(i))
print(j,type(j))
print(k,type(k))
print(l,type(l))
print(m,type(m))
print(n,type(n))
print(o,type(o))
print("End of second section")