# https://projecteuler.net/problem=9

def special_pythagorean_triplet(sum: int) -> int:
    for a in range(3, (sum - 3) // 3):
        for b in range(a, sum - 1 - a):
            c = 1000 - b - a
            if c < 1:
                continue

            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

print(special_pythagorean_triplet(1000))
