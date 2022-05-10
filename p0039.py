# https://projecteuler.net/problem=39

def how_many_pythagorean_triplet(perimeter: int) -> int:
    result = 0

    for a in range(3, (perimeter - 3) // 3):
        for b in range(a, perimeter - 1 - a):
            c = perimeter - b - a
            if c < 1:
                continue

            if a ** 2 + b ** 2 == c ** 2:
                result += 1

    return result


assert how_many_pythagorean_triplet(120) == 3

print(max((how_many_pythagorean_triplet(p), p) for p in range(3, 1001))[1])
