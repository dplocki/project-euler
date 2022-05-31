# https://projecteuler.net/problem=64

from math import floor
from typing import Iterator

def period_length_continued_fraction_representations_of_square_root(n: int) -> Iterator[int]:
    a0 = floor(n ** 0.5)
    if a0 * a0 == n:
        return 0

    was = set()

    m = 0
    d = 1
    a = a0

    while (m, d) not in was:
        was.add((m, d))

        m = d * a - m
        d = (n - m * m) // d
        a = floor((a0 + m) / d)

    return len(was) - 1

print(sum(1
    for n in range(1, 10_000)
    if period_length_continued_fraction_representations_of_square_root(n) % 2 == 1
))
