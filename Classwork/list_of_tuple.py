def create_tuple(l1, l2):
    result = list(zip(l1, l2))
    return result


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10, 11]

answer = create_tuple(l1, l2)
print(answer)


def create_tuple(list1, list2):
    result = []

    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")

    for i in range(len(list1)):
        result.append((list1[i], list2[i]))

    return result


l1 = [1, -2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

answer = create_tuple(l1, l2)
print(answer)

