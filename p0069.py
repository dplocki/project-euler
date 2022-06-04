# https://projecteuler.net/problem=69

from functools import cache
from itertools import count
from math import sqrt
from typing import Iterator

@cache
def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n))+2):
        if n % i == 0:
            return False

    return True

def prime_generator() -> Iterator[int]:
    yield 2
    for candidate in count(3, step=2):
        if is_prime(candidate):
            yield candidate

def inversed_totient_maximum(limit: int) -> int:
    n = 1
    for prime in prime_generator():
        if prime * n > limit:
            return n
        
        n *= prime

assert inversed_totient_maximum(10) == 6
print(inversed_totient_maximum(1_000_000))
