num = int(input('enter a number'))
for x in range(1, 13):

    times = "x"
    equal = "="
    for y in range(1, num + 1):

        print(f'{x:>2} {times:>2} {y:>2} {equal:>2} {x * y:>2}', end='\t\t')
    print()