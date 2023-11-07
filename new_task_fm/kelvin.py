def check_for_subsequence(word, words):
    checker = 0
    checker2 = 0
    while checker < len(word) and checker2 < len(words):
        if words[checker2] == word[checker]:
            checker += 1
        checker2 += 1
    return checker == len(word)


print(check_for_subsequence("123", "1142534561"))
print(check_for_subsequence("ace", "abcde"))
print(check_for_subsequence("met", "trime"))
print(check_for_subsequence("ace", "ecace"))
print(check_for_subsequence("ace", "casace"))
