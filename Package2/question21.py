def divisible_and_multiple(start, end):
    for x in range(start, end + 1):
        if x % 7 == 0 and x % 5 == 0:
            print(x)


divisible_and_multiple(1500, 2700)


def divisible_and_multiple2(x):
    if x % 7 == 0 and x % 5 == 0:
        print("Divisible by 7 and multiple of 5")
    else:
        print("Not divisible by 7 and not a multiple of 5")


divisible_and_multiple(1500)
divisible_and_multiple(2700)
