# https://projecteuler.net/problem=1

def simple_solution(upper_limit: int) -> int:
    return sum(n for n in range(upper_limit) if n % 3 == 0 or n % 5 == 0)

def better_solution(upper_limit: int) -> int:

    def sum_of_divisible_by(divisible: int):
        last_divisible = (upper_limit - 1) // divisible
        return divisible * last_divisible * (last_divisible + 1) // 2

    return sum_of_divisible_by(3) + sum_of_divisible_by(5) - sum_of_divisible_by(15)

LIMIT = 1000
assert simple_solution(LIMIT) == better_solution(LIMIT)
