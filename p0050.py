# https://projecteuler.net/problem=50

from array import array
from math import isqrt

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

def consecutive_prime_sum(limit: int) -> int:
    primes = sieve(limit)
    primes_as_set = set(primes)
    all_primes_sum = sum(primes)
    all_primes_number = len(primes)

    base = all_primes_sum
    for window_size in range(len(primes) - 1, 1, -1):
        base -= primes[window_size]

        current_base = base
        if current_base < limit and current_base in primes_as_set:
            return current_base

        for i in range(1, all_primes_number - window_size):
            current_base -= primes[i - 1]
            current_base += primes[i + window_size - 1]
    
            if current_base < limit and current_base in primes_as_set:
                return current_base

assert consecutive_prime_sum(100) == 41
assert consecutive_prime_sum(1_000) == 953
print(consecutive_prime_sum(1_000_000))
