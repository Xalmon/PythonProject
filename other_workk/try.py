def test2(check_even):
    return check_even % 2 == 0


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(test2, lst1)))


def test3(multiple):
    return multiple ** 2


print(list(map(test3, lst1)))

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = [counter for counter in lst1 if counter % 2 == 0]
answer1 = [test3(counter) for counter in lst1]
answer2 = [counter % 2 == 0 for counter in lst1]
print(answer)
print(answer1)
print(answer2)

ans = (m for m in lst1 if m % 2 == 0)
print(ans)

mul = [n ** 2 for n in lst1]
print(mul)

print(list(map(lambda quick: quick ** 2, lst1)))


