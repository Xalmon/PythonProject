with open('../other_workk/account.txt', mode='w') as my_file:
    my_file.write('001 esther 15\n')
    my_file.write('002 moyin 16\n')
    my_file.write('003 precious 17\n')
    my_file.write('004 ashley 18\n')
    my_file.write('005 grace 20\n')

with open('../other_workk/account.txt', mode='r') as my_file:
    print(my_file.read())

