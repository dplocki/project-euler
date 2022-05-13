# https://projecteuler.net/problem=49

from itertools import combinations, permutations
from typing import Tuple

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

def prime_permutations() -> Tuple[int, int, int]:
    primes = set(number for number in range(1000, 10000) if is_prime(number))

    already_checked = set()
    for prime in primes:
        if prime in already_checked:
            continue

        all_permutations = set(int(''.join(x for x in permutation)) for permutation in permutations(str(prime)))
        only_prime_permutations = sorted(permutation for permutation in all_permutations if permutation in primes)
        already_checked.update(only_prime_permutations)

        if len(only_prime_permutations) < 3:
            continue

        yield from (combination
            for combination in combinations(only_prime_permutations, 3)
            if combination[2] - combination[1] == combination[1] - combination[0])

for prime_permutation in prime_permutations():
    if prime_permutation[0] != 1487:
        print(''.join(str(p) for p in prime_permutation))
