# https://projecteuler.net/problem=52

from itertools import count

def sort_digitaze(number: int) -> list[str]:
    return sorted(str(number))

def find_the_smallest_permuted_multiples():
    for x in count(1):
        digits_of_x = sort_digitaze(x)
        
        if all(sort_digitaze(x * multiplayer) == digits_of_x for multiplayer in range(6, 0, -1)):
            return x

print(find_the_smallest_permuted_multiples())
