tuple1 = ("apple", "banana", "cherry")
l_tuple = list(tuple1)
l_tuple[1] = "kiwi"
tuple1 = tuple(l_tuple)

print(tuple1)