import includes.standard_lib as lib

print("LIST: ")
lib.showcase_list()
print("")

print("TUPLE: ")
a = int(input("Number1: "))
b = int(input("Number2: "))
lib.showcase_tuple(a, b)
print("")

print("EQUATION: ")
print(lib.calculate_eq(1, 2, 3))
