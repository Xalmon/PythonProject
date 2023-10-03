user_input = input("Enter the alphanumeric sentence/word: ")


def extract_numbers(input_string):
    largest = second_largest = float('-inf')

    for char in input_string:
        if char.isdigit():
            digit = int(char)
            if digit > largest:
                second_largest = largest
                largest = digit
            elif digit > second_largest and digit < largest:
                second_largest = digit

    if second_largest != float('-inf'):
        print("The second largest digit in the string is:", second_largest)
    else:
        print("There is no second largest digit in the string.")


extract_numbers(user_input)
