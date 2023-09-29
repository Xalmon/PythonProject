def calculate_int(input_string):
    total_sum = 0

    for char in input_string:
        if char.isdigit():
            total_sum += int(char)

    return total_sum


string_input = "A12BCKDT52"
sum_of_int = calculate_int(string_input)

print("Sample input:", string_input)
print("Sample output:", sum_of_int)
