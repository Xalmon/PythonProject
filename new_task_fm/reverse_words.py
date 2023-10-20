def reverse_words(input_str):
    words = input_str.split()
    reversed_words = []

    for reverse in words:
        reversed_word = ""
        for counter in range(len(reverse) - 1, -1, -1):
            reversed_word += reverse[counter]
        reversed_words.append(reversed_word)

    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence


word = "solomon oyefule"
word2 = "A better place"
word3 = "switch off Moyin's phone"
print(reverse_words(word))
print(reverse_words(word2))
print(reverse_words(word3))
