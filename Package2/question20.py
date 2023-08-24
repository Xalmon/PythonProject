def check_and_print_color(color_list_1, color_list_2):
    common_colors = color_list_1 & color_list_2
    common_colors = [color.capitalize() for color in common_colors]

    if common_colors:
        print(', '.join(common_colors))
    else:
        print("No common colors found.")


Test_Data = set(["white", "Black", "Red"])
Test_Data2 = set(["Red", "Green"])

check_and_print_color(Test_Data, Test_Data2)
