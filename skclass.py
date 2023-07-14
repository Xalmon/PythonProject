# def main():
#
#     sum1(10)
#     sum1(20)
#     sum1(15)
#
#
# def sum1(number):
#     total = 0
#     for counter in range(1, number + 1):
#         total += counter
#     print(total)
#
#
# main()

def greater(number1, number2, number3, number4):
    maximum = number1
    if number2 > maximum:
        maximum = number2
    if number3 > maximum:
        maximum = number3
    if number4 > maximum:
        maximum = number4
    return maximum


result = greater(7, 8, 7, 7)
print("The largest is", {result})


def lesser(number1, number2, number3, number4):
    minimum = number1
    if number2 < minimum:
        minimum = number2
    if number3 < minimum:
        minimum = number3
    if number4 < minimum:
        minimum = number4
    return minimum


result = lesser(1, 5, 2, 8)
print("The smallest is", {result})
