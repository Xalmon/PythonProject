def reverse_name(x):
    words = x.split()
    reversed_words = []

    for reverse in words:
        reversed_word = ""
        for counter in range(len(reverse) - 1, -1, -1):
            reversed_word += reverse[counter]
        reversed_words.append(reversed_word)

    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


word = "solomon oyefule"
print(reverse_name(word))
