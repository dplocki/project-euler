# https://projecteuler.net/problem=60

from typing import List, Set
from array import array
from functools import cache, reduce
from itertools import takewhile
from math import isqrt, sqrt

def sieve(num: int) -> array:
    # https://codereview.stackexchange.com/questions/222518/prime-sieve-in-python

    flags = bytearray(num)      # Initially, all bytes are zero
    flags[2] = 1                # Two is prime

    for i in range(3, num, 2):
        flags[i] = 1            # Odd numbers are prime candidates

    # Find primes and eliminate multiples of those primes
    for i in range(3, isqrt(num) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return array('I', (i for i, flag in enumerate(flags) if flag))

def check(a: int, b: int) -> int:
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

@cache
def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n))+2):
        if n % i == 0:
            return False

    return True

def backtracking(checked_primes: Set[int], collection: List[int]) -> List[int]:
    previous = collection[-1] if collection else 0

    for prime in checked_primes:
        if prime <= previous:
            continue

        if all(check(prime, x) for x in collection):
            yield from backtracking(checked_primes, collection + [prime])

    yield collection

def prime_pair_sets() -> int:
    primes = sieve(1_000_000)
    checked_primes = list(takewhile(lambda prime: prime < 10_000, primes))

    for pairs_set in backtracking(checked_primes, []):
        length, sum_of_all = reduce(lambda result, current: (result[0] + 1, result[1] + current), pairs_set, (0, 0))
        if length == 5:
            return sum_of_all

print(prime_pair_sets())
