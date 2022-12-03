# https://projecteuler.net/problem=79

from functools import reduce
from itertools import permutations
from typing import Generator, Iterable, Tuple

def load_input() -> Generator[Tuple[int, int, int], None, None]:
    with open('p079_keylog.txt', 'r') as file:
        for line in file.readlines():
            yield tuple(int(c) for c in line.strip())

def check_permutation(unique_attempts: Iterable[Tuple[int, int, int]], permutation: Tuple[int, ...]) -> bool:
    for check in unique_attempts:
        first_digit = permutation.index(check[0])
        second_digit = permutation.index(check[1])
        third_digit = permutation.index(check[2])

        if not (first_digit < second_digit < third_digit):
            return False

    return True

def solution(input) -> int:
    unique_attempts = set(input)
    unique_digits = reduce(lambda a, b: a.union(b), unique_attempts, set())

    for permutation in permutations(unique_digits, len(unique_digits)):
        if check_permutation(unique_attempts, permutation):
            return ''.join(map(str, permutation))


input = load_input()
print(solution(input))
