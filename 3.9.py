num = int(input("Enter a five-digit integer: "))


digit_1 = num // 10000
digit_2 = (num // 1000) % 10
digit_3 = (num // 100) % 10
digit_4 = (num // 10) % 10
digit_5 = num % 10

print(f"Digits: {digit_1} {digit_2} {digit_3} {digit_4} {digit_5}")
