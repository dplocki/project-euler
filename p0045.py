# https://projecteuler.net/problem=45

def triangle(n: int) -> int:
    return n * (n + 1) // 2

def pentagonal(n: int) -> int:
    return n * (3 * n - 1) // 2

def hexagonal(n: int) -> int:
    return n * (2 * n - 1)

def find_equal_for_triangle(t: int, p: int, h: int) -> int:
    while True:
        triangle_number = triangle(t)
        pentagonal_number = pentagonal(p)
        hexagonal_number = hexagonal(h)

        if pentagonal_number < triangle_number:
            p += 1
            continue

        if hexagonal_number < triangle_number:
            h += 1
            continue

        if triangle_number == pentagonal_number == hexagonal_number:
            return triangle_number
        
        t += 1

print(find_equal_for_triangle(285 + 1, 165, 143))
