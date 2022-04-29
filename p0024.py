# https://projecteuler.net/problem=24

from itertools import permutations

for _, p in zip(range(1_000_000), permutations('0123456789')):
    pass

print(''.join(p))
