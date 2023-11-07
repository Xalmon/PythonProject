number = [8, 2, 5, 6, 1, 3, 9, 4, 7]


def reverse_list(x):
    for num in range(len(number)):
        for num2 in range(len(number)):
            if number[num2] <= number[num]:
                number[num2], number[num] = number[num], number[num2]
    return x


print(reverse_list(number))

number = [8, 2, 5, 6, 1, 3, 9, 4, 7, 9]
print(number[::-1])

