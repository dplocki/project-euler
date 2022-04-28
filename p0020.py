# https://projecteuler.net/problem=20

def factorial(n: int) -> int:
    if n == 1:
        return 1

    return n * factorial(n - 1)

def factorial_digit_sum(n: int) -> int:
    return sum(int(digit) for digit in str(factorial(n)))

assert factorial(10) == 3628800
assert factorial_digit_sum(10) == 27
print(factorial_digit_sum(100))
