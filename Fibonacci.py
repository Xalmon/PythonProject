def fibonacci(x):
    sequence = [0, 1]

    for _ in range(2, x):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence


x = 10
Sequence = fibonacci(x)
print("Fibonacci sequence: ", Sequence)
