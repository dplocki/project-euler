# https://projecteuler.net/problem=5

from collections import Counter
from functools import reduce
from operator import mul

def prime_factors(n: int) -> list[int]:
    while n % 2 == 0:
        yield 2
        n = n // 2
         
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i== 0:
            yield i
            n = n // i

    if n > 2:
        yield n

def smallest_multiple(up_to_divisible: int) -> int:
    factors_table = {}

    for divisible in range(2, up_to_divisible):
        factors = Counter(prime_factors(divisible))
        for factor, count_of_factor in factors.items():
            if factors_table.get(factor, 0) > count_of_factor:
                continue

            factors_table[factor] = count_of_factor

    return reduce(mul, (factor ** exponent for factor, exponent in factors_table.items()))


assert smallest_multiple(10) == 2520
print(smallest_multiple(20))
