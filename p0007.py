# https://projecteuler.net/problem=7

def is_prime(n: int) -> bool:
    if n < 4:
        return True

    if n % 2 == 0:
        return False

    if n < 9:
        return True

    if n % 3 == 0:
        return False

    r = int(n ** 0.5)
    f = 5

    while f <= r:
        if n % f == 0:
            return False

        if n % (f+2) == 0:
            return False

        f += 6

    return True

def nth_prime(n: int) -> int:
    count = 1
    candidate = 1
    while count < n:
        candidate = candidate + 2

        if is_prime(candidate):
            count = count + 1

    return candidate

assert nth_prime(6) == 13
print(nth_prime(10001))
