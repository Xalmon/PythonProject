def concatenate_all_element_to_string(lst):
    concatenated_string = ''.join(str(element) for element in lst)
    return concatenated_string


my_list = [1, 2, 3, 'a', 'b', 'c']


result = concatenate_all_element_to_string(my_list)
print(result)

