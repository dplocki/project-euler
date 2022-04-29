# https://projecteuler.net/problem=25

def fibonacci() -> list[int]:
    a = 1
    b = 1
    while True:
        yield a
        a, b = b, a + b

def find_index_with_n_digits(n: int) -> int:
    digts = 10 ** (n - 1) - 1

    for index, term in enumerate(fibonacci()):
        if term > digts:
            return index + 1

assert find_index_with_n_digits(3) == 12
print(find_index_with_n_digits(1000))
