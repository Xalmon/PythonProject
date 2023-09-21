# user_input = input("Enter the numbers: ")
#
#
# def remove_duplicate_numbers(input_string):
#     input_string = input_string.split()
#     duplicate = []
#
#     for counter in input_string:
#         if counter not in duplicate:
#             return counter
#
#
# print(remove_duplicate_numbers([2, 2, 1]))
# print(remove_duplicate_numbers([4, 3, 2, 2, 3, 3]))


def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# print(find_single_number([2, 2, 1]))
print(find_single_number([4, 3, 2, 2, 3, 3]))
# print(find_single_number([1]))
