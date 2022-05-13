# https://projecteuler.net/problem=46

from itertools import count

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

def twice_square(x: int) -> int:
    return 2 * x ** 2

def goldbachs_other_conjecture():
    primes = set()
    primes.add(2)

    double_squares = set()
    double_squares.add(twice_square(0))
    double_squares.add(twice_square(1))
    add_n_for_double_squares = 2
    next_double_square = twice_square(add_n_for_double_squares)

    for number in count(3, step=2):
        if is_prime(number):
            primes.add(number)

        if next_double_square <= number:
            double_squares.add(next_double_square)
            add_n_for_double_squares += 1
            next_double_square = twice_square(add_n_for_double_squares)

        if all((number - ds) not in primes for ds in double_squares):
            return number

print(goldbachs_other_conjecture())
