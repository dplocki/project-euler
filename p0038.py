# https://projecteuler.net/problem=38

def pandigital_multiples():
    result = ''

    for n in range(2, 10):
        for interger in range(1, 10 ** (9 // 2)):
            candidate = ''.join(str(i * interger) for i in range(1, n + 1))
            candidate_digits = set(candidate)

            if '0' in candidate_digits or len(candidate) != 9 or len(candidate_digits) != 9:
                continue

            if candidate > result:
                result = candidate

    return result

print(pandigital_multiples())
