# https://projecteuler.net/problem=51

from functools import cache
from itertools import count

@cache
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    if n < 4:
        return True

    if n % 2 == 0:
        return False

    if n < 9:
        return True

    if n % 3 == 0:
        return False

    r = int(n ** 0.5)
    i = n - 2
    while i >= r:
        if n % i == 0:
            return False

        i -= 2

    return True

def prime_generator(start: int) -> list[int]:
    for number in count(start, step=2):
        if not is_prime(number):
            continue

        yield number

def prime_digit_replacements() -> int:
    checked = set()
    for prime in prime_generator(9_999):
        if prime in checked:
            continue

        prime_as_str = str(prime)
        for digit in '012':
            if prime_as_str.count(digit) != 3:
                continue

            result = 0
            for replacement in '0123456789':
                number_after_replacement = int(prime_as_str.replace(digit, replacement))
                checked.add(number_after_replacement)

                if number_after_replacement > 10_000 and is_prime(number_after_replacement):
                    result += 1

            if result == 8:
                return prime

print(prime_digit_replacements())
