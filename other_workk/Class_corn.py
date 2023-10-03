# def highest_odd(x):
#     if x % 2 == 0:
#         return x
# def greater(number1, number2, number3, number4, number5, number6, number7, number8, number9):
#     maximum = number1
#     if number2 > maximum:
#         maximum = number2
#     if number3 > maximum:
#         maximum = number3
#     if number4 > maximum:
#         maximum = number4
#     if number5 > maximum:
#         maximum = number5
#     if number6 > maximum:
#         maximum = number6
#     if number7 > maximum:
#         maximum = number7
#     if number8 > maximum:
#         maximum = number8
#     if number9 > maximum:
#         maximum = number9
#     return maximum
# result = greater(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print("The largest is", {result})


numbers = [1, 2, 11, 4, 5, 6, 107, 8, 9, 10]
answer = [counter for counter in numbers if counter % 2 != 0]
# answer2 = [counter for counter in answer if counter > 8]
# print(answer2)
print(max(answer))


# def check_duplicate(x):
#     for x in []:
#         if [0] in x == [1]:
#             return x
#         elif [1] in x == [2]:
#             return x
#         elif [2] in x == [3]:
#             return x
#         elif [3] in x == [4]:
#             return x
#         else:
#             return "no duplicate"
#
#
# fruits = ["apple", "grape", "orange", "banana", "apple"]
# print(check_duplicate(fruits))


def check_duplicate(x):
    seen = set()
    for item in x:
        if item in seen:
            return item
        seen.add(item)
    return "no duplicate"


fruits = ["apple", "grape", "orange", "banana", "apple"]
print(check_duplicate(fruits))

