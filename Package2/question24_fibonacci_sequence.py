def fibonacci(fibo):
    sequence = [0, 1]

    for _ in range(2, fibo):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


fibo1 = 10
Sequence = fibonacci(fibo1)
print("Fibonacci sequence: ", Sequence)


def generate_fibonacci_sequence(limit):
    sequence = [0, 1]

    while True:
        next_term = sequence[-1] + sequence[-2]

        if next_term > limit:
            break

        sequence.append(next_term)

    return sequence


limit = 50

fibonacci_sequence = generate_fibonacci_sequence(limit)
print("Fibonacci sequence up to", limit, ":")
print(fibonacci_sequence)
