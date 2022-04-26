# https://projecteuler.net/problem=10

def is_prime(n: int) -> bool:
    if n == 1:
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
    f = 5

    while f <= r:
        if n % f == 0:
            return False

        if n % (f + 2) == 0:
            return False

        f += 6

    return True

def sum_before(limit: int) -> int:
    result = 2
    candidate = 3

    while candidate < limit:
        if is_prime(candidate):
            result += candidate

        candidate += 2

    return result

assert sum_before(10) == 17

print(sum_before(2_000_000))
