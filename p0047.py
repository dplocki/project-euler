# https://projecteuler.net/problem=47

from collections import deque
from functools import reduce
from itertools import count

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

def distinct_primes_factors(window_size: int) -> int:
    window = deque(set(prime_factors(n + 2)) for n in range(window_size))

    for number in count(window_size + 2):
        window.popleft()
        window.append(set(prime_factors(number)))

        if all(len(primes) >= window_size for primes in window) and len(reduce(lambda result, primes: result & primes, window)) == 0:
            return number - window_size + 1

assert distinct_primes_factors(2) == 14
assert distinct_primes_factors(3) == 644
print(distinct_primes_factors(4))
