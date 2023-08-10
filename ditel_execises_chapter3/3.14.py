pi_estimate = 4.0
sign = -1
term = 3.0

terms_needed = []

print(f"{'Number of Terms':<15}{'Approximation of Pi':<15}")

for pi in range(1, 11):
    pi_estimate += sign * (4 / term)
    term += 2
    sign *= -1

    print(f"{pi:<15}{pi_estimate:<15.10f}")

    if abs(pi_estimate - 3.14) < 0.00001:
        terms_needed.append(pi)

print("\nNumber of terms needed for specific approximations:")
# print(f"Approximation 3.14: {terms_needed[0]}")
# print(f"Approximation 3.141: {terms_needed[1]}")
# print(f"Approximation 3.1415: {terms_needed[2]}")
# print(f"Approximation 3.14159: {terms_needed[3]}")
