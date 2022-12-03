# https://projecteuler.net/problem=26

from typing import Generator, Tuple
import math

def unit_fraction_decimal_part(d: int) -> Generator[int, None, None]:
    multiplayer = 10 ** math.ceil(math.log10(d)) 
    from_what = multiplayer

    while from_what != 0:
        digit = from_what // d
        yield digit
        from_what = (from_what - digit * d) * multiplayer

    yield None

class GeneratorCache:
    def __init__(self, generator_function) -> None:
        self.generator_function = generator_function
        self.cache = {}
        self.last_index = -1
        self.is_ended = False

    def get_value_for(self, index: int) -> int:
        if self.is_ended:
            return None

        if index > self.last_index:
            for i in range(self.last_index + 1, index + 1):
                tmp = next(self.generator_function)
                if tmp == None:
                    self.is_ended = True
                    return None

                self.cache[i] = tmp

            self.last_index = index

        return self.cache[index]

def floyd(generator_cache: GeneratorCache) -> Tuple[int, int]:
    index = 1
    while generator_cache.get_value_for(index) != generator_cache.get_value_for(index * 2):
        index += 1
   
    if generator_cache.is_ended:
        return 0, 0

    cycle_start = 0
    hare_index = index
    tortoise_index = 0
    while generator_cache.get_value_for(tortoise_index) != generator_cache.get_value_for(hare_index):
        hare_index += 1
        tortoise_index += 1
        cycle_start += 1
 
    cycle_length = 1
    hare_index = tortoise_index + 1
    while generator_cache.get_value_for(tortoise_index) != generator_cache.get_value_for(hare_index):
        hare_index += 1
        cycle_length += 1

    return cycle_length, cycle_start

def get_reciprocal_cycle_length(n: int) -> int:
    return floyd(GeneratorCache(unit_fraction_decimal_part(n)))[0]

def find_d_with_longest_cycle(limit: int) -> int:
    best_max = 0
    best_d = 0

    for d in range(2, limit):
        g = GeneratorCache(unit_fraction_decimal_part(d))
        current_reciprocal_cycle_length = floyd(g)[0]
        if current_reciprocal_cycle_length > best_max:
            best_max = current_reciprocal_cycle_length
            best_d = d

    return best_d

print(find_d_with_longest_cycle(1000))
