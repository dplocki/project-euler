# https://projecteuler.net/problem=66

from math import floor
from operator import itemgetter
from typing import Iterator, List

def period_continued_fraction_representations_of_square_root(n: int) -> Iterator[int]:
    a0 = floor(n ** 0.5)
    if a0 * a0 == n:
        return

    m = 0
    d = 1
    a = a0
    yield a0
    was = set()

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = floor((a0 + m) / d)

        if (m, d) not in was:
            was.add((m, d))
            yield a
        else:
            return

def numerator(d_period: List[int], n: int) -> int:
    n_table = { -2: 0, -1: 1 }

    for i in range(n + 1):
        n_table[i] = d_period[i] * n_table[i - 1] + n_table[i - 2]

    return n_table[n]

def find_minimal_x(d: int):
    d_period = list(period_continued_fraction_representations_of_square_root(d))
    k = len(d_period) - 1
    
    if k == -1:
        return 0
    if k % 2 == 0:
        return numerator(d_period, k - 1)
    else:
        return numerator(d_period + d_period[1:-1], 2 * k - 1)

def largest_value_of_minimal_solutions(max_d: int):
    return max(((d, find_minimal_x(d)) for d in range(max_d + 1)), key=itemgetter(1))[0]

assert largest_value_of_minimal_solutions(7) == 5
print(largest_value_of_minimal_solutions(1_000))
