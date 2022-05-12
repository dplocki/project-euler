# https://projecteuler.net/problem=43

from itertools import permutations

def sub_string_divisibility():
    for permutation in permutations(range(10), 10):
        if permutation[3] % 2 != 0:
            continue

        if permutation[5] != 0 and permutation[5] != 5:
            continue

        if (permutation[2] + permutation[3] + permutation[4]) % 3 != 0:
            continue

        if (100 * permutation[4] + 10 * permutation[5] + permutation[6]) % 7 != 0:
            continue

        if (100 * permutation[5] + 10 * permutation[6] + permutation[7]) % 11 != 0:
            continue

        if (100 * permutation[6] + 10 * permutation[7] + permutation[8]) % 13 != 0:
            continue

        if (100 * permutation[7] + 10 * permutation[8] + permutation[9]) % 17 != 0:
            continue

        yield int(''.join(str(d) for d in permutation))


print(sum(sub_string_divisibility()))
