# https://projecteuler.net/problem=57

from typing import List, Tuple

def div_one(factor: Tuple[int, int]) -> Tuple[int, int]:
    return factor[1], factor[0]

def add_integer(factor: Tuple[int, int], integer: int) -> Tuple[int, int]:
    return factor[1] * integer + factor[0], factor[1]

def square_root_convergents() -> List[Tuple[int, int]]:
    factor = (1, 2)

    while True:
        yield add_integer(factor, 1)
        factor = div_one(add_integer(factor, 2))

print(sum(
        1
        for (numerator, denominator), _ in zip(square_root_convergents(), range(1_000))
        if len(str(numerator)) > len(str(denominator))))
