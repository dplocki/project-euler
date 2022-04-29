# https://projecteuler.net/problem=23

from functools import reduce
from operator import mul
from itertools import product, combinations_with_replacement
from collections import Counter

def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n

def get_divisors(n):
    pf = prime_factors(n)
    pf_with_multiplicity = Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in product(*powers):
        yield reduce(mul, prime_power_combo)

abundant_numbers = set(i for i in range(2, 28124) if sum(get_divisors(i)) - i > i)
abundant_numbers_sums = set(a + b for a, b in combinations_with_replacement(abundant_numbers, 2))

print(sum(i for i in range(28124) if not i in abundant_numbers_sums))
