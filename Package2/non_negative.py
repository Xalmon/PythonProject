def check_non_negative_integer(n):
    return isinstance(n, int) and n >= 0


values = [42, -5, "apple", 0, 7, "banana", -3, 9.8, 18, "cherry"]

non_negative_integers = [val for val in values if check_non_negative_integer(val)]

for val in non_negative_integers:
    print(val)
