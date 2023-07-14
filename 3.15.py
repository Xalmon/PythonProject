e_estimate = 1.0
factorial = 1.0

for i in range(1, 11):
    factorial *= i
    term = 1.0 / factorial
    e_estimate += term

print(f"Estimate of e after summing 10 terms: {e_estimate}")
