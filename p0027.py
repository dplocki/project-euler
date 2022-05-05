# https://projecteuler.net/problem=27

from functools import cache

@cache
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n < 4:
        return True

    if n % 2 == 0:
        return False

    if n < 9:
        return True

    if n % 3 == 0:
        return False

    r = int(n ** 0.5)
    i = n - 2
    while i >= r:
        if n % i == 0:
            return False

        i -= 2

    return True

def number_of_consecutive_primes(a: int, b: int) -> int:
    n = 2

    while is_prime(n * n + a * n + b):
        n += 1

    return n

assert number_of_consecutive_primes(1, 41) == 40
assert number_of_consecutive_primes(-79, 1601) == 80

max_product = 0
max_primes = 0
for a in range(-999, 1001, 2):
    for b in range(3, 1001, 2):
        primes_lenght = number_of_consecutive_primes(a, b)
        if primes_lenght > max_primes:
            max_primes = primes_lenght
            max_product = a * b

print(max_product)
