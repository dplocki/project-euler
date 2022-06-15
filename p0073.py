# https://projecteuler.net/problem=73

from typing import Tuple

def farey_next(n: int, a: int, b: int, c: int, d: int) -> Tuple[int, int, int, int]:
    k = (n + b) // d
    return c, d, k * c - a, k * d - b

def find_numerator_after(n: int, a: int, b: int) -> int:
    result = n
    
    while (1 + a * result) % b != 0:
        result -= 1

    return result

def counting_fractions_in_range(n: int) -> int:
    a = 1
    b = 3
    d = find_numerator_after(n, a, b)
    c = (1 + a * d) // b

    result = -1
    while a != 1 or b != 2:
        a, b, c, d = farey_next(n, a, b, c, d)
        result += 1

    return result

assert counting_fractions_in_range(8) == 3
print(counting_fractions_in_range(12_000))
