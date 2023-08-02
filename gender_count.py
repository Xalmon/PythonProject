def count_gender(sample_lists):
    count_female = 0
    count_male = 0
    for sample in sample_lists:
        if sample.casefold() == 'female':
            count_female += 1
        elif sample.casefold() == 'male':
            count_male += 1

    new_list = [['Male', count_male], ['Female', count_female]]
    return new_list


sample_list = ['Male', 'Female', 'female', 'male', 'male', 'male', 'Female', 'male', 'Female', 'Male', 'Female', 'Male',
               'female']
result = count_gender(sample_list)
print(result)
