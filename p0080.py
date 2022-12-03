# https://projecteuler.net/problem=80
from decimal import getcontext, Decimal
from math import sqrt

def str_to_digit_sum(n) -> int:
    return sum(map(int, n))

def solution():
    getcontext().prec = 102

    return sum(
        str_to_digit_sum(str(Decimal(number + 1).sqrt()).replace('.', '')[:100])
        for number in range(100)
        if not sqrt(number + 1) % 1 == 0
    )

print(solution())
