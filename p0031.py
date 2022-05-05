# https://projecteuler.net/problem=31

def different_ways_number(coins_set: tuple, wanted_amount: int) -> int:
    result = { 0: 1 }

    for coin in coins_set:
        for a in range(wanted_amount + 1):
            result[a] = result.get(a, 0) + result.get(a - coin, 0)

    return result[wanted_amount]

print(different_ways_number((1, 2, 5, 10, 20, 50, 100, 200), 200))
