# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.


# String Methods 
# capitalize()	Converts the first character to upper case
a = "graduation day"
print(a.capitalize()) 

# casefold()	Converts string into lower case
b = "GRADUATION DAY"
print(b.casefold())

# center()	Returns a centered string
c = "graduation"
print(c.center(20, '-'))

# count()	Returns the number of times a specified value occurs in a string
d = "graduation day graduation"
print(d.count("graduation"))

# encode()	Returns an encoded version of the string
e = "graduation day"
print(e.encode())

# endswith()	Returns true if the string ends with the specified value
f = "graduation day"
print(f.endswith("day"))

# expandtabs()	Sets the tab size of the string
g = "graduation\tday"
print(g.expandtabs(10))

# find()	Searches the string for a specified value and returns the position of where it was found
h = "graduation day"
print(h.find("day"))

# format()	Formats specified values in a string
i = "Welcome to {}"
print(i.format("Graduation Day"))

# format_map()	Formats specified values in a string
j = "Welcome to {event}"
print(j.format_map({"event": "Graduation Day"}))

# index()	Searches the string for a specified value and returns the position of where it was found
k = "graduation day"
print(k.index("day"))

# isalnum()	Returns True if all characters in the string are alphanumeric
l = "graduation2026"
print(l.isalnum())

# isalpha()	Returns True if all characters in the string are in the alphabet
m = "graduation"
print(m.isalpha())

# isascii()	Returns True if all characters in the string are ascii characters
n = "graduation day!"
print(n.isascii())

# isdecimal()	Returns True if all characters in the string are decimals
o = "202SIX"
print(o.isdecimal())

# isdigit()	Returns True if all characters in the string are digits
p = "2O26"
print(p.isdigit())

# isidentifier()	Returns True if the string is an identifier
q = "graduation_day"
print(q.isidentifier())

# islower()	Returns True if all characters in the string are lower case
r = "graduation day"
print(r.islower())

# isnumeric()	Returns True if all characters in the string are numeric
s = "2O26"
print(s.isnumeric())

# isprintable()	Returns True if all characters in the string are printable
t = "graduation day!\n"
print(t.isprintable())

# isspace()	Returns True if all characters in the string are whitespaces
u = "   "
print(u.isspace())

# istitle()	Returns True if the string follows the rules of a title
v = "Graduation Day"
print(v.istitle())

# isupper()	Returns True if all characters in the string are upper case
w = "GRADUATION DAY"
print(w.isupper())

# join()	Joins the elements of an iterable to the end of the string
x = ["Graduation", "Day", "2026"]
print(" ".join(x))

# ljust()	Returns a left justified version of the string
y = "graduation"
print(y.ljust(20, '-'))

# lower()	Converts a string into lower case
z = "GRADUATION DAY"
print(z.lower())

# lstrip()	Returns a left trim version of the string
aa = "   graduation day   "
print(aa.lstrip())

# maketrans()	Returns a translation table to be used in translations
ab = "graduation day"
converted = str.maketrans("g", "6")
print(ab.translate(converted))

# partition()	Returns a tuple where the string is parted into three parts
ac = "graduation day"
print(ac.partition("day"))

# replace()	Returns a string where a specified value is replaced with a specified value
ad = "graduation day"
print(ad.replace("day", "ceremony"))

# rfind()	Searches the string for a specified value and returns the last position of where it was found
ae = "graduation day graduation"
print(ae.rfind("graduation"))

# rindex()	Searches the string for a specified value and returns the last position of where it was found
af = "graduation day graduation"
print(af.rindex("graduation"))

# rjust()	Returns a right justified version of the string
ag = "graduation"
print(ag.rjust(20, '-'))

# rpartition()	Returns a tuple where the string is parted into three parts
ah = "graduation day"
print(ah.rpartition("day"))

# rsplit()	Splits the string at the specified separator, and returns a list
ai = "graduation day graduation"
print(ai.rsplit(" ", 1))

# rstrip()	Returns a right trim version of the string
aj = "   graduation day   "
print(aj.rstrip())

# split()	Splits the string at the specified separator, and returns a list
ak = "graduation day graduation"
print(ak.split(" "))

# splitlines()	Splits the string at line breaks and returns a list
al = "graduation day\ngood luck"
print(al.splitlines())

# startswith()	Returns true if the string starts with the specified value
am = "graduation day"
print(am.startswith("graduation"))

# strip()	Returns a trimmed version of the string
an = "   graduation day   "
print(an.strip())

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
ao = "Graduation DAY"
print(ao.swapcase())

# title()	Converts the first character of each word to upper case
ap = "graduation day"
print(ap.title())

# translate()	Returns a translated string
aq = "graduation day"
converted = str.maketrans("g", "9")
print(aq.translate(converted))

# upper()	Converts a string into upper case
ar = "graduation day"
print(ar.upper())

# zfill()	Fills the string with a specified number of 0 values at the beginning
at = "2026"
print(at.zfill(10))

# end of python_string_methods.py

