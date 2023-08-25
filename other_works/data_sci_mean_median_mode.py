from statistics import median


values = [9, 11, 22, 34, 17, 22, 34, 22, 40]


mean_value = sum(values) / len(values)


sorted_values = sorted(values)
mid_index = len(sorted_values) // 2


if len(sorted_values) % 2 == 0:
    median_value = (sorted_values[mid_index - 1] + sorted_values[mid_index]) / 2
else:
    median_value = sorted_values[mid_index]


def calculate_mode(values_list):
    value_count = {}
    for value in values_list:
        value_count[value] = value_count.get(value, 0) + 1

    max_count = max(value_count.values())
    mode_value = [key for key, value in value_count.items() if value == max_count]

    return mode_value


mode_value = calculate_mode(values)

print(f"Mean: {mean_value:.2f}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
