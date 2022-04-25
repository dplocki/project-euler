# https://projecteuler.net/problem=2

def fibonacci() -> list[int]:
    a = 0
    b = 1

    while True:
        a, b = b, a + b
        yield b

def even_fibonacci_numbers(limit:int=4_000_000) -> int:
    result = 0
    for f in fibonacci():
        if f >= limit:
            break

        if f % 2 == 0:
            result += f

    return result 

print(even_fibonacci_numbers())
