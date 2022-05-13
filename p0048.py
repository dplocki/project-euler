# https://projecteuler.net/problem=48

def self_powers(limit: int) -> int:
    return sum(i ** i for i in range(1, limit + 1))

assert self_powers(10) == 10405071317
print(str(self_powers(1000))[-10:])
