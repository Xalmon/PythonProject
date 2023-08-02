def check_list(x):
    for num in range(len(number)):
        for num2 in range(len(number)):
            if number[num2] > number[num]:
                number[num2], number[num] = number[num], number[num2]
    return x


number = [100, 22, 35, 40, 50]

number = check_list(number)

print("element: ", number)
