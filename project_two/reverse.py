def reverse_name(x):
    words = x.split()
    reversed_words = []

    for word in words:
        reversed_word = ""
        for i in range(len(word) - 1):
            reversed_word += word[i]
        reversed_words.append(reversed_word)

    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


word = "solomon oyefule"
print(reverse_name(word))
