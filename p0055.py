# https://projecteuler.net/problem=54

from functools import cache

ITERATIONS_LIMIT = 50

@cache
def is_palindromic(number: int) -> bool:
    tmp = str(number)
    return tmp == tmp[::-1]

def digitize(n: int) -> list[int]:
    while n > 0:
        yield n % 10
        n //= 10

@cache
def is_lychrel_number(number: int) -> bool:
    for _ in range(ITERATIONS_LIMIT):
        digits = list(digitize(number))
        number += sum(10 ** multiplayer * digit for multiplayer, digit in enumerate(reversed(digits)))
        if is_palindromic(number):
            return False

    return True

assert is_lychrel_number(47) == False
assert is_lychrel_number(196) == True

print(sum(1 for i in range(1, 10_000) if is_lychrel_number(i)))
