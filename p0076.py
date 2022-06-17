# https://projecteuler.net/problem=76

def counting_summations(n: int) -> int:
    cache = { 0: 1 }

    for number in range(1, n):
        for i in range(1, n + 1):
            cache[i] = cache.get(i, 0) + cache.get(i - number, 0)

    return cache[n]

assert counting_summations(5) == 6
print(counting_summations(100))
