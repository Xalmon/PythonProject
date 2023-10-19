def mounting_zeros2(lst):
    number = 0
    for counter in range(len(lst)):
        if lst[counter] != 0:
            lst[counter], lst[number] = lst[number], lst[counter]
            number += 1
    return lst


print(mounting_zeros2([0, 4, -3, 0, 2, 0, 4, 10, 12]))
