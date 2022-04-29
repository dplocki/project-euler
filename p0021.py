# https://projecteuler.net/problem=21

from functools import reduce
from operator import mul
from itertools import product
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

def d(n):
    return sum(get_divisors(n)) - n

assert d(220) == 284

all_divisors_sum = {i:d(i) for i in range(2, 10_000)}

print(sum(k for k, v in all_divisors_sum.items() if k != v and k == all_divisors_sum.get(v, 0)))
