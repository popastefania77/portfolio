"""
Write a generator that implements the Fibonacci algorithm.

Fibonacci sequence = series of numbers where each number is the sum of the two preceding ones.
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
"""


def fibonacci_algorithm_generator(n):
    yield 0
    if n > 0:
        yield 1
    if n > 1:
        for i in range(2, n + 1):
            yield (i - 1) + (i - 2)


for element in fibonacci_algorithm_generator(10):
    print(element, end=' ')
