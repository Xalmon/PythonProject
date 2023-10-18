def is_anagram2(first_letter, second_letter):
    if len(first_letter) != len(second_letter):
        return False
    char_counts = {}
    for char in first_letter:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for char in second_letter:
        if char in char_counts:
            char_counts[char] -= 1
        else:
            return False
    return all(count == 0 for count in char_counts.values())


print(is_anagram2("nagaram", "anagram"))