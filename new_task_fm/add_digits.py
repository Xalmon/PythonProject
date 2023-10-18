import math
# class AddDigits:
#     def sum_digits(self, strings):
#         digits = [int(counter) for counter in strings]
#         while len(digits) > 1:
#             digits = [int(counter2) for counter2 in str(sum(digits))]
#         return digits[0]
#
#
# if __name__ == '__main__':
#     add_digit = AddDigits()
#     result = add_digit.sum_digits("99")
#     print(result)


num = 38
num_str = str(num)
num_digits = len(num_str)
print(num_digits)
new_val = 0
for counter in num_str:
    new_val += int(counter)
print(new_val)

