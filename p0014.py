# https://projecteuler.net/problem=14

def next_collatz_generator(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return n * 3 + 1

def lenght_of_collatz_for(cache: dict, n: int) -> int:
    if n == 1:
        return 1

    if n in cache:
        return cache[n]

    result = 1 + lenght_of_collatz_for(cache, next_collatz_generator(n))
    cache[n] = result
    return result

cache = {}
the_longest_chain_length = 1
the_longest_chain_start =  1

for starting_number in range(2, 1_000_000):
  length = lenght_of_collatz_for(cache, starting_number)
  if length > the_longest_chain_length:
      the_longest_chain_length = length
      the_longest_chain_start = starting_number

print(the_longest_chain_start)
