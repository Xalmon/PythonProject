print('{:>8}{:>8}{:>8}'.format('Number', 'Square', 'Cube'))
print('{:>8}{:>8}{:>8}'.format('------', '------', '----'))

for num in range(6):
    square = num ** 2
    cube = num ** 3
    print('{:>8}{:>8}{:>8}'.format(num, square, cube))
