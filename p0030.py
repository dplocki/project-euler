# https://projecteuler.net/problem=30

from functools import cache

def digits(n: int) -> list[int]:
    while n:
        yield n % 10
        n //= 10

@cache
def five_power_of_digit(d: int) -> int:
    return d ** 5

print(sum(n for n in range(2, 5 * five_power_of_digit(9) + 1) if sum(five_power_of_digit(d) for d in digits(n)) == n))
