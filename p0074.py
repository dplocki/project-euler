# https://projecteuler.net/problem=74

from functools import cache
from math import factorial

ASCII_ZERO = ord('0')

@cache
def sum_factorial_of_digits(n: int):
    return sum(factorial(ord(d) - ASCII_ZERO) for d in str(n))

def count_not_repeating_chain(n: int) -> int:
    chains = set()

    while n not in chains:
        chains.add(n)
        n = sum_factorial_of_digits(n)

    return len(chains)

print(sum(1 for n in range(1_000_000) if count_not_repeating_chain(n) == 60))
