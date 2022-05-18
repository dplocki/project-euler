# https://projecteuler.net/problem=56

print(max(
    sum(map(int, str(a ** b)))
    for a in range(1, 100)
    for b in range(1, 100)))
