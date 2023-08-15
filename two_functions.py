# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# intersection = find_intersection_test(list1, list2)
# print(intersection)


def find_intersection(list_one, list_two):
    return tuple(set(list_one) & set(list_two))


list1 = ["solomon", 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]

intersection = find_intersection(list1, list2)
print(intersection)
