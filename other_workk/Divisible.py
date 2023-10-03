import math


def divide_or_square(number):
    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return round(number % 5, 2)


print(divide_or_square(10))
print(divide_or_square(9))
