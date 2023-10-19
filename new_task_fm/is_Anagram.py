def anagram(word, word1):
    if len(word) != len(word1):
        return False
    if sorted(word) == sorted(word1):
        return True
    return False


s = "madam"
t = "mdaam"

print(anagram(s, t))


def is_anagram3(word, word1):
    if len(word) != len(word1):
        return False

    for counter in word:

        if counter not in word1:
            return False

    return True


print("anagram d 3'rd", "=", anagram("madam", "damam"))

