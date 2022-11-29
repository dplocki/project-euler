# https://projecteuler.net/problem=77

from functools import cache
from itertools import count
from typing import Generator

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

def prime_generator() -> Generator[int, None, None]:
    yield 2
    for number in count(3, step=2):
        if not is_prime(number):
            continue

        yield number

def solution(limit: int) -> int:
    primes_source = prime_generator()
    results = { (1, 2): 0, (2, 2): 1 }
    primes = [ next(primes_source) ]
    current_column = 2

    for new_prime in primes_source:
        previous_prime = primes[-1]

        for column in range(current_column + 1, new_prime + 1):
            results[column, 2] = results[column - 2, 2]
            for current_row, previous_row in zip(primes[1:], primes):
                results[column, current_row] = results.get((column - current_row, current_row), 0) + results.get((column, previous_row), 0)
                if results[column, current_row] > limit:
                    return column

        primes.append(new_prime)

        for n in range(1, new_prime):
            results[n, new_prime] = results.get((n, previous_prime), 0)

        results[new_prime, new_prime] = results.get((new_prime, previous_prime), 0) + 1
        current_column = new_prime

print(solution(5_000))
