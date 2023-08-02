def names_check_capitalization(sample_lst, letter):
    statement = {}
    for sample in sample_lst:
        if sample.casefold().startswith(letter):
            word = sample.casefold()
            if word not in statement:
                statement[word] = 1
            else:
                statement[word] += 1
    return statement


sample_list = ["Seyi", " Seyi", "Seye", "sodiq", "Samanta", "sabrina", "Kiki", "jane", "uloma"]
word = 's'
result = names_check_capitalization(sample_list, word)
print(result)
