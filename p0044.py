# https://projecteuler.net/problem=44

def pentagon_numbers():
    n = 1
    while True:
        yield n * (3 * n - 1) // 2
        n += 1

def is_pentagonal(x: int) -> bool:
  return ((1 + 24 * x) ** 0.5) % 6 == 5

def the_minimaze_pentagon_numbers() -> int:
    previous_pentagon_numbers = set()
    for pentagon_number in pentagon_numbers():
        for p in previous_pentagon_numbers:
            sum = p + pentagon_number
            difference = pentagon_number - p

            if difference in previous_pentagon_numbers and is_pentagonal(sum):
                return difference

        previous_pentagon_numbers.add(pentagon_number)

print(the_minimaze_pentagon_numbers())
