# https://projecteuler.net/problem=75

from collections import defaultdict
from math import gcd, isqrt
from typing import Iterator, Tuple

def triplets_stefan(N: int) -> Iterator[Tuple[int, int, int]]:
    for m in range(isqrt(N - 1) + 1):
        for n in range(1 + m % 2, min(m, isqrt(N - m * m) + 1), 2):
            if gcd(m, n) > 1:
                continue

            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            for k in range(1, N // c + 1):
                yield k * a, k * b, k * c

MAXIUM_L = 1_500_000
triaplets = defaultdict(int)
for a, b, c in triplets_stefan(MAXIUM_L + 1):
    wire_length = a + b + c

    if wire_length <= MAXIUM_L:
        triaplets[wire_length] += 1

print(sum(1 for value in triaplets.values() if value == 1))
