for i in range(4):
    num = int(input(f"Enter integers : "))

sum_nums = sum(num)

average = sum_nums / 4

product = 1
for num in num:
    product *= num

smallest = min(num)
largest = max(num)

print(f"Sum: {sum_nums}")
print(f"Average: {average}")
print(f"Product: {product}")
print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
