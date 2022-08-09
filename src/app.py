from math import *
from unicodedata import name

a = 3
b = float(input("Enter a number: "))

c = a + b + (a * b) + max(a, b)
print(pow(c, 2))

names = ["Vito", "Sonny", "Tom", "Michael"]
print(names)
print(len(names))
print(names[0] + " " + names[1])
print(names[2:])
print(names[1:3])
names[1] = "Fredo"
print(names)
names.append("Sonny")
print(names)
names.insert(2, "Tessio")
print(names)
names.remove("Fredo")
names.append("Clemenza")
print(names)
names.sort()
print(names)
names.reverse()
print(names)

names2 = names.copy()
names2.insert(0, "Fredo")
print(names2)
print(names)
