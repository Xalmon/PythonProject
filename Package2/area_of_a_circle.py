import math


def area_circle():
    radius = float(input("Enter the radius: "))

    area = math.pi * radius ** 2
    print("Circumference:", area)


area_circle()
