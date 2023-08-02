total = 0
total1 = 1
number = [10, 20, 30, 40, 50]
for counter in range(0, len(number)):
    total = total + number[counter]
print("Sum of all elements in given list: ", total)

for counter in range(0, len(number)):
    total1 += number[counter]
print("Square of all elements in given list: ", total1)