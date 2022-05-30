# https://projecteuler.net/problem=63

from itertools import count

def numbers():
    for base in range(1, 10):
        for exponentiation in count(1):
            number = base ** exponentiation
            digits_count = len(str(number))

            if digits_count == exponentiation:
                yield 1
            else:
                break

print(sum(numbers()))
