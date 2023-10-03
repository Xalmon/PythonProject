for num in range(100):
    if num % 3 == 0 and num % 5 == 0:
        print("Fizz_Buzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
