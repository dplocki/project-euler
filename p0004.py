# https://projecteuler.net/problem=4

from itertools import combinations

def is_palindrome(number: int) -> bool:
    number_as_string = str(number)

    return number_as_string[::-1] == number_as_string

def only_palindrome_product(start: int, end: int) -> list[int]:
    x = list(range(start, end + 1))

    for a, b in combinations(x, 2):
        tmp = a * b
        if is_palindrome(tmp):
            yield tmp

def the_largest_palindrome(start: int, end: int) -> int:
    return sorted(only_palindrome_product(start, end), reverse=True)[0]

assert is_palindrome(12345) == False
assert is_palindrome(123321) == True
assert the_largest_palindrome(10, 99) == 9009

print(the_largest_palindrome(100, 999))
