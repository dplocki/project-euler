# https://projecteuler.net/problem=80
from math import sqrt

PRECISION = 100

def str_to_digit_sum(n) -> int:
    return sum(map(int, n))

def square_root(n, digits):
    limit = 10**(digits + 1)
    a = 5*n
    b = 5
    while b < limit:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b//10) * 100 + 5

    return b // 100

def solution():
    return sum(
        str_to_digit_sum(str(square_root(number + 1, PRECISION)))
        for number in range(PRECISION)
        if not sqrt(number + 1) % 1 == 0
    )

print(solution())
