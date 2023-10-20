def check_for_unique_char(word, word2):
    if len(word) != len(word2):
        return False
    if "#" not in word or "#" not in word2:
        return False
    index1 = word.index("#")
    index2 = word2.index("#")
    if index1 != index2 or word[index1+1] != "#" or word2[index2+1] != "#":
        return False
    return word[index1-1] == word2[index2-1] and word[index1+2] == word2[index2+2]


print(check_for_unique_char("a#b#dpqrs#", "ac#d##pqr"))
