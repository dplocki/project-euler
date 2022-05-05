# https://projecteuler.net/problem=28

def number_spiral_diagonals(n: int) -> int:
    size = n // 2 + 2

    a = sum(4 * x * x - 4 * x + 1 for x in range(1, size))
    b = sum(4 * x * x - 10 * x + 7 for x in range(1, size))
    c = sum(4 * x * x - 8 * x + 5 for x in range(1, size))
    d = sum(4 * x * x - 6 * x + 3 for x in range(1, size))

    return a + b + c + d - 3

assert number_spiral_diagonals(5) == 101
print(number_spiral_diagonals(1001))
