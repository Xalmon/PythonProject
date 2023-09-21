def sum_list(lists, value):
    result = []
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if lists[i] + lists[j] == value:
                result.extend([i, j])
    return result


l1 = [5, 4, 9, 7, 2, 0]
target = 16

answer = sum_list(l1, target)
print(answer)
