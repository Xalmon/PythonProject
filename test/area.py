import math


def area_check(radius):
    area_of_circle = math.pi * (radius ** 2)

    if radius < 0:
        raise ValueError("Radius cannot be negative")

    if type(radius) is not int and type(radius) is not float:
        raise TypeError("not an int")
    else:
        return area_of_circle


area_check(6)
