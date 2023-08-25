def calculate_pi(num_terms):
    pi_approx = 0
    sign = 1

    for i in range(1, num_terms * 2, 2):
        pi_approx += sign * (4 / i)
        sign *= -1

    return pi_approx


def main():
    target_pi_values = [3.14, 3.141, 3.1415, 3.14159]
    terms_required = []

    for target in target_pi_values:
        num_terms = 1
        while True:
            approx_pi = calculate_pi(num_terms)
            if approx_pi >= target:
                terms_required.append(num_terms)
                break
            num_terms += 1

    print("Terms required to approximate π to different values:")
    for i, target in enumerate(target_pi_values):
        print(f"π ≈ {calculate_pi(terms_required[i]):.5f} using {terms_required[i]} terms for {target}")


if __name__ == "__main__":
    main()
