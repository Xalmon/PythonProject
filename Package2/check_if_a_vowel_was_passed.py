import re


def check_if_vowel_was_passed(word):
    if re.search("[aeiou]", word):
        print("i sense the presence of a VOWEL")
    else:
        print("Bunch of consonants")


print(check_if_vowel_was_passed("bbb"))
