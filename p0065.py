# https://projecteuler.net/problem=65

from functools import cache

def a_from_position(n: int) -> int:
    if n == 0:
        return 2

    return (2 * (n + 1) // 3) if (n - 1) % 3 == 1 else 1

@cache
def numerator(n: int) -> int:
    if n == -2:
        return 0
    
    if n == -1:
        return 1

    return a_from_position(n) * numerator(n - 1) + numerator(n - 2)

def sum_digits_in_nth_numerator(n: int) -> int:
    return sum(int(digit) for digit in str(numerator(n -1)))

assert sum_digits_in_nth_numerator(10) == 17
print(sum_digits_in_nth_numerator(100))
