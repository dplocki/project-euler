# https://projecteuler.net/problem=12

def triangles_number() -> list[int]:
    internal_counter = 1
    number = 0

    while True:
        number += internal_counter
        yield number
        internal_counter += 1

def factors(n: int) -> list[int]:
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            yield i
            yield n // i

def highly_divisible_triangular_number(whanted_diviable_number: int) -> int:
    for triangle_number in triangles_number():
        triangle_number_factors = set(factors(triangle_number))
        if len(triangle_number_factors) > whanted_diviable_number:
            return triangle_number

assert highly_divisible_triangular_number(5) == 28
print(highly_divisible_triangular_number(500))
