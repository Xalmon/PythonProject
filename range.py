for counter in range(5):
    for counter1 in range(5 - counter):
        print(' ', end=' ')
    for counter1 in range(counter + 1):
        print(' ', end='*')
    for counter1 in range(counter + 1):
        print('*', end=' ')
    print('')
for counter in range(5):
    for counter1 in range(counter + 1):
        print(' ', end=' ')
    for counter1 in range(5 - counter):
        print(' ', end='*')
    for counter1 in range(5 - counter):
        print('*', end=' ')
    print('')
