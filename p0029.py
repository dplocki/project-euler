# https://projecteuler.net/problem=29

from itertools import product

def distinct_powers(max: int) -> int:
    return len(set(a ** b for a, b in product(range(2, max + 1), repeat=2)))

assert distinct_powers(5) == 15
print(distinct_powers(100))
