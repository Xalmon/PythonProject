def check_for_unique_char(word):
    checker = []
    for char in word:
        if char != "#":
            checker.append(char)
        else:
            checker.pop()
    return "".join(checker)


def compare_lists(word, words):
    if check_for_unique_char(word) == check_for_unique_char(words):
        return True
    else:
        return False


print(compare_lists("ab#d", "ac#d"))
print(compare_lists("aq##", "c#d#"))
print(compare_lists("aq#", "r"))
print(compare_lists("a#b#d#pqrs#", "ac#d##pqr"))
