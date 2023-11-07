def check_for_subsequence(word, words):
    checker = 0
    checker2 = 0
    while checker < len(word) & checker2 < len(words):
        if words[checker] == word[checker2]:
            checker += 1

        checker2 += 1
    wild_card = checker == len(words)

    return wild_card


print(check_for_subsequence("123", "1425"))
print(check_for_subsequence("ace", "abcde"))
