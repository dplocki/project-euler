# https://projecteuler.net/problem=40

from functools import reduce
from operator import mul

def digitaze(n: int) -> int:
    while n > 0:
        yield n % 10
        n //= 10      

def get_digit_on_th_position(position: int) -> int:
    limit_previous = 1
    digit_counter = 1
    base = 1

    while True:
        limit = limit_previous + digit_counter * 9 * base

        if position < limit:
            number = (position - limit_previous) // digit_counter + base
            position_digit = (position - limit_previous) % digit_counter

            return list(digitaze(number))[- position_digit - 1]

        limit_previous = limit
        digit_counter += 1
        base *= 10

assert get_digit_on_th_position(1) == 1
assert get_digit_on_th_position(12) == 1

print(reduce(mul, (get_digit_on_th_position(10**i) for i in range(7))))
