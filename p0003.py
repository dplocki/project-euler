# https://projecteuler.net/problem=3

from math import gcd

def factorization(number: int) -> int:

    def get_factor(number: int) -> int:
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for _ in range(cycle_size):
                if factor > 1:
                    break

                x = (x * x + 1) % number
                factor = gcd(x - x_fixed, number)

            cycle_size *= 2
            x_fixed = x

        return factor

    while number > 1:
        next = get_factor(number)
        yield next
        number //= next


def largest_prime_factor(number: int) -> int:
    return sorted(factorization(number), reverse=True)[0]

assert largest_prime_factor(13195) == 29
print(largest_prime_factor(600851475143))
