check = set(range(5))
print(check)

x = range(0, 10)
check = set(x)
print(check)

check = {10, 20, 30}
check.add(40)
print(check)

check = {10, 20, 30}
check1 = [40, 50, 60, 10]
check.update(check1, range(5))
print(check)

check = {40, 10, 30, 20}
check.remove(30)
print(check)

red = range(10, 20)
indigo = range(20, 30)
blue = set(red)
yellow = set(indigo)
answer = {counter for counter in indigo if counter % 2 != 0}
answer1 = {counter for counter in indigo if counter % 2 == 0}
print(answer)
print(answer1)


sii = {"bird", "cat", "dog"}
sii.remove("bird")
sii.add("goat")
sii.add("bat")
sii.add("ninja")
sii.discard("dog")
print(sii)

print(blue.issubset(yellow))
print(blue.issuperset(yellow))
print(blue | yellow)
print(blue & yellow)
