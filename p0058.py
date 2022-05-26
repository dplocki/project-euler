# https://projecteuler.net/problem=58

from math import sqrt
from functools import cache
from typing import List, Tuple

@cache
def is_prime(n):
    for i in range(2, int(sqrt(n))+2):
        if n % i == 0:
            return False

    return True

def corners_generator():
    spiral_side_size = 1
    point = 3

    while True:
        yield point
        spiral_side_size += 1

        point += spiral_side_size
        yield point

        point += spiral_side_size
        yield point

        spiral_side_size += 1

        point += spiral_side_size
        yield point - 1

        point += spiral_side_size

def split_into_four(generator: List[int]) -> List[Tuple[int, int, int, int]]:
    while True:
        yield next(generator), next(generator), next(generator), next(generator)

def find_side_size_less_10_percent():
    primes_number = 0
    non_primes_number = 1

    for ne, nw, se, _ in split_into_four(corners_generator()):
        if is_prime(ne):
            primes_number += 1
        else:
            non_primes_number += 1

        if is_prime(nw):
            primes_number += 1
        else:
            non_primes_number += 1

        if is_prime(se):
            primes_number += 1
        else:
            non_primes_number += 1

        non_primes_number += 1

        if primes_number / (primes_number + non_primes_number) < 0.1:
            return nw - ne + 1

print(find_side_size_less_10_percent())
