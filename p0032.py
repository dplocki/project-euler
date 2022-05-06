# https://projecteuler.net/problem=32

from itertools import permutations
from typing import Tuple

def add_only_pandigital(permutation: Tuple, first_break: int, second_break: int) -> int:
    p = ''.join(str(i) for i in permutation)
    product = int(p[second_break:])
    if int(p[:first_break]) * int(p[first_break:second_break]) == product:
        return product
    
    return 0

possibilities = [(fb, sb) for fb in range(1, 8) for sb in range(fb + 1, 9)]
numbers = set(add_only_pandigital(p, fb, sb) for p in permutations(range(1, 10), 9) for fb, sb in possibilities)

print(sum(numbers))
