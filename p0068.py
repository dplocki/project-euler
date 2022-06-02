# https://projecteuler.net/problem=68

from itertools import permutations
from token import STAR
from typing import Iterator, List, Tuple

STAR = {
    0: (5, 6),
    1: (6, 7),
    2: (7, 8),
    3: (8, 9),
    4: (9, 5),
}

def find_all_solutions() -> Iterator[Tuple]:
    for p in permutations(range(1, 10)):
        if p[0] + p[4] + p[5] == p[1] + p[5] + p[6] == p[2] + p[6] + p[7] == p[3] + p[7] + p[8] == 10 + p[8] + p[4]:
            yield list(p[:4]) + [10] + list(p[4:])

def translate(postions: List[int]):
    starting_point = postions.index(min(postions[:5]))

    result = ''
    for i in range(5):
        current_angle = (starting_point + i) % 5
        result += str(postions[current_angle])
        for digit_index in STAR[current_angle]:
            result += str(postions[digit_index])

    return int(result)

print(max(map(translate, find_all_solutions())))
