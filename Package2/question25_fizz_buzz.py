def fizz_buzz():
    result_list = []

    for num in range(100):
        if num % 3 == 0 and num % 5 == 0:
            result_list.append("Fizz_Buzz")
        elif num % 3 == 0:
            result_list.append("Fizz")
        elif num % 5 == 0:
            result_list.append("Buzz")
        else:
            result_list.append(num)

    print(result_list)


fizz_buzz()
