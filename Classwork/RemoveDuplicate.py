lasts = [1, 2, 3, 2, 4, 5, 6, 1, 2]


def remove_duplicate2(input_list):
    input_list = [0]
    [x for x in input_list if x != input_list]
    return input_list


print(remove_duplicate2(lasts))

