# https://projecteuler.net/problem=35

import array
from math import floor, isqrt, log10

def sieve(num):
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

    return array.array('I', (i for i, flag in enumerate(flags) if flag))

def digitize(n: int) -> list[int]:
    while n > 0:
        yield n % 10
        n //= 10

def rotate_number(n: int) -> int:
    lenght = floor(log10(n))

    for _ in range(lenght):
        n = (n % 10) * 10 ** lenght + (n // 10)
        yield n

def find_circular_primes_number(limit: int) -> int:
    primes = set(sieve(limit))
    return sum(1
        for prime in primes
        if all(
            p in primes
            for p in rotate_number(prime)))

assert find_circular_primes_number(100) == 13 
print(find_circular_primes_number(1_000_000))
