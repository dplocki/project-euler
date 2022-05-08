# https://projecteuler.net/problem=37

from functools import cache

@cache
def is_prime(n: int) -> bool:
    if n < 2:
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
    f = 5

    while f <= r:
        if n % f == 0:
            return False

        if n % (f+2) == 0:
            return False

        f += 6

    return True

def is_truncatable_prime_from_right(n: int) -> bool:
    while n > 0:
        if not is_prime(n):
           return False

        n //= 10

    return True

def truncatable_primes():
    candidates = [ 2, 3, 5, 7 ]
    multiplayer = 10

    while len(candidates) > 0:
        new_candidates = []

        for candidate in candidates:

            for digit in range(1, 10):
                prime_candidate = digit * multiplayer + candidate

                if is_truncatable_prime_from_right(prime_candidate):
                    yield prime_candidate

                if is_prime(prime_candidate):
                    new_candidates.append(prime_candidate)

        candidates = new_candidates
        multiplayer *= 10

assert is_truncatable_prime_from_right(3797) == True

print(sum(prime for _, prime in zip(range(11), truncatable_primes())))
