for counter in range(10):
    for counter1 in range(counter + 1):
        print('@', end=' ')
    for counter1 in range(10 - counter):
        print(' ', end=' ')
    for counter1 in range(10 - counter):
        print('@', end=' ')
    for counter1 in range(counter + 1):
        print(' ', end=' ')
    for counter1 in range(counter + 1):
        print(' ', end=' ')
    for counter1 in range(10 - counter):
        print('@', end=' ')
    for counter1 in range(10 - counter):
        print(' ', end=' ')
    for counter1 in range(counter + 1):
        print('@', end=' ')
    print()

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print(total)

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print(total)

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers[0::2]:
    total += number
print(total)

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers[0::4]:
    total += number
print(total)

numbers = [100, 22, 35, 40, 50]
numbers_square = [counter ** 2 for counter in numbers]
total = max(numbers_square)
total1 = min(numbers_square)
print(numbers_square.sort())
print(numbers_square)
print(total1)
print(total)

numbers = [10, 20, 30, 40, 50]
numbers_square1 = [counter + + 2 for counter in numbers]
print(numbers_square1)

numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
sort = sorted(numbers)
print(sort)

number = [8, 2, 5, 6, 1, 3, 9, 4, 7]


def check_list(x):
    for num in range(len(numbers)):
        for num2 in range(len(numbers)):
            if numbers[num2] > numbers[num]:
                numbers[num2], numbers[num] = numbers[num], numbers[num2]
    return x


def even_number(x):
    new_x = []
    for number2 in x:
        if number2 % 2 == 0:
            new_x.append(numbers)
    return new_x


question = [counter2 for counter2 in number if counter2 % 2 == 0]
print(question)
print(even_number(numbers))
print(check_list(numbers))


def reverse_list(x):
    for num in range(len(numbers)):
        for num2 in range(len(numbers)):
            if numbers[num2] <= numbers[num]:
                numbers[num2], numbers[num] = numbers[num], numbers[num2]
    return x


print(reverse_list(numbers))

number4 = [8, 2, 5, 6, 1, 3, 9, 4, 7]
print(numbers[::-1])
