# https://projecteuler.net/problem=61

from typing import List, Set
from functools import reduce
from itertools import dropwhile, permutations, takewhile

def triangle():
    n = 1
    while True:
        yield n * (n + 1) // 2
        n += 1

def square():
    n = 1
    while True:
        yield n ** 2
        n += 1

def pentagonal():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1

def hexagonal():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1

def heptagonal():
    n = 1
    while True:
        yield n * (5 * n - 3) // 2
        n += 1

def octagonal():
    n = 1
    while True:
        yield n * (3 * n - 2)
        n += 1

def only_four_cycle_able_digits(generator):
    yield from filter(lambda x: (x % 100) > 10, takewhile(lambda x: x < 10_000, dropwhile(lambda x: x < 1_000, generator)))

def find_cyclic_to_number(candidates: List[int], n: int) -> List[int]:
    right_part_of_n = n % 100

    yield from (candidate for candidate in candidates if (candidate // 100) == right_part_of_n)

def backtracking(candidates_numbers: Set[int], chains: List[int]):
    if len(chains) == 5:
        yield chains + [100 * (chains[4] % 100) + (chains[0] // 100)]
        return

    generate = find_cyclic_to_number(candidates_numbers, chains[-1]) \
        if len(chains) > 0 \
        else candidates_numbers

    for candidate in generate:
        yield from backtracking(candidates_numbers, chains + [candidate])

def cyclical_figurate_numbers():
    fours_digits_numbers = [set(only_four_cycle_able_digits(triangle())),
        set(only_four_cycle_able_digits(square())),
        set(only_four_cycle_able_digits(pentagonal())),
        set(only_four_cycle_able_digits(hexagonal())),
        set(only_four_cycle_able_digits(heptagonal())),
        set(only_four_cycle_able_digits(octagonal()))]

    for proposition in backtracking(reduce(lambda a, b: a | b, fours_digits_numbers), []):
        for permutation in permutations(proposition):
            if all(p in s for p, s in zip(permutation, fours_digits_numbers)):
                return sum(permutation)

print(cyclical_figurate_numbers())
