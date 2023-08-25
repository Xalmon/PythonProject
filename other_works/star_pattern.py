size = int(input("Enter the size of the diamond: "))


for i in range(1, size + 1):
    print(' ' * (size - i) + '*' * (2 * i - 1))


for i in range(size - 1, 0, -1):
    print(' ' * (size - i) + '*' * (2 * i - 1))
