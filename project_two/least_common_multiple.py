def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


num1 = 12
num2 = 18

result = lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {result}")
