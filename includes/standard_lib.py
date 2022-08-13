from math import *


def showcase_tuple(a, b):  # Showcases example function for tuples
    p1 = (a, b)
    p2 = (3, 4)
    print(p1)
    print(p2[0])
    print(p2[1])
    p3 = (0.4, 0.5, 0.1)
    print(p3)
    points = [p1, p2, p3]
    print(points)


def showcase_list():  # Showcases example function for lists
    names = ["Vito", "Sonny", "Tom", "Michael"]
    print(names)
    print(len(names))
    print(names[0] + " " + names[1])
    print(names[2:])
    print(names[1: 3])
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


def showcase_dictionary():  # Showcases example function for dictionaries
    options = {
        "A": "New Game",
        "B": "Options",
        "C": "Quit"
    }
    print(options["B"])
