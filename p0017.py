# https://projecteuler.net/problem=17

AND_LENGHT = len('and')
NUMBERS_LENGHT = {
    0: len('zero'),
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('nine'),

    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nineteen'),

    20: len('twenty'),
    30: len('thirty'),
    40: len('forty'),
    50: len('fifty'),
    60: len('sixty'),
    70: len('seventy'),
    80: len('eighty'),
    90: len('ninety'),
    100: len('onehundred'),
    1000: len('onethousand')
}

def count_letter_number(n: int) -> int:
    if n in NUMBERS_LENGHT:
        return NUMBERS_LENGHT[n]

    if n > 100:
        result = NUMBERS_LENGHT[n // 100] + (NUMBERS_LENGHT[100] - NUMBERS_LENGHT[1])
        if n % 100 == 0:
            return result
        else:
            return result + AND_LENGHT + count_letter_number(n % 100)

    if n > 10:
        return NUMBERS_LENGHT[n % 10] + NUMBERS_LENGHT[n - (n % 10)]

def number_letter_counts(how_much: int) -> int:
    return sum(count_letter_number(i) for i in range(1, how_much + 1))

assert count_letter_number(342) == 23
assert count_letter_number(115) == 20

assert number_letter_counts(5) == 19

print(number_letter_counts(1000))
