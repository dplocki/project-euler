# https://projecteuler.net/problem=62

from itertools import count

def cubic_permutations(permutations_counter: int) -> int:
    result = {}

    for n in count(10):
        cube_hash = ''.join(sorted(str(n ** 3)))

        cube_permutations = result.get(cube_hash, set())
        cube_permutations.add(n)

        result[cube_hash] = cube_permutations

        if len(cube_permutations) == permutations_counter:
            return sorted(cube_permutations)[0] ** 3

assert cubic_permutations(3) == 41063625
print(cubic_permutations(5))
