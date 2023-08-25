def calculate_max_heart_rate(age):
    return 220 - age


def calculate_target_heart_rate_range(max_heart_rate):
    lower_target_rate = max_heart_rate * 0.5
    upper_target_rate = max_heart_rate * 0.85
    return lower_target_rate, upper_target_rate


age = int(input("Please enter your age: "))

max_heart_rate = calculate_max_heart_rate(age)
print("Your maximum heart rate:", max_heart_rate, "beats per minute")

lower_target_rate, upper_target_rate = calculate_target_heart_rate_range(max_heart_rate)
print("Your target heart rate range:", lower_target_rate, "to", upper_target_rate, "beats per minute")
