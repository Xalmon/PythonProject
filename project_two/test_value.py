def test_value_in_list(test_data, value):
    for sublist in test_data:
        if value in sublist:
            return True
    return False


Test_Data = [[1, 5, 8, 3], [1, 5, 8, 3]]

value1 = 3
result1 = test_value_in_list(Test_Data, value1)
print(f"{value1} -> {Test_Data} {result1}")

value2 = -1
result2 = test_value_in_list(Test_Data, value2)
print(f"{value2} -> {Test_Data} {result2}")
