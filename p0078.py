# https://projecteuler.net/problem=78

from functools import cache
from itertools import cycle, count

def k_generate():
    delta_a = 1
    delta_b = 1
    index = 0

    while True:
        index += delta_a
        yield index
        delta_a += 2

        index += delta_b
        yield index
        delta_b += 1

@cache
def p(n: int) -> int:
    if n == 0 or n == 1:
        return 1

    get_k = k_generate()
    get_sign = cycle([1, 1, -1, -1])
    result = 0

    while True:
        k = next(get_k)
        if k > n:
            break

        result += next(get_sign) * p(n - k)

    return result

def solution():
    for n in count(1):
        if p(n) % 1_000_000 == 0:
            return n

assert p(5) == 7
print(solution())
