# https://projecteuler.net/problem=41

from functools import cache
from itertools import permutations

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

def the_largest_pandigital_prime():
    for n in range(7, 1, -1):
        digits = (str(p) for p in range(n, 0, -1))
        for permutation in permutations(digits, n):
            number = int(''.join(permutation))
            if is_prime(number):
                return number

print(the_largest_pandigital_prime())
