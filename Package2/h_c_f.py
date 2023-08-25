def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)


num1 = 12
num2 = 18

result_hcf = hcf(num1, num2)
print(f"HCF of {num1} and {num2} is {result_hcf}")
