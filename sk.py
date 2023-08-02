x = int(input("Enter a number: "))

if x % 2 == 0:
    print(f"number {x} is Even")
else:
    print(f'number {x} is Odd')
num = int(input("Enter number: "))

print(num % 2 == 0)


def check_even(Input):
    if Input % 2 == 0:
        print(f"number {Input} is Even")
    else:
        print(f'number {Input} is Odd')


check_even(max(98, 65, 100, 30, 69, 44))
check_even(987)
check_even(100)
check_even(69)
check_even(30)
