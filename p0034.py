# https://projecteuler.net/problem=34

from math import factorial

def find_up_maximum():
    digit_length = 1

    while True:
        maximum_sum = digit_length * factorial(9)
        
        if maximum_sum > int(digit_length * '9'):
            digit_length += 1
        else:
            return maximum_sum

def digitize(n: int) -> list[int]:
    while n > 0:
        yield n % 10
        n //= 10

print(sum(number
    for number in range(10, find_up_maximum() + 1)
    if sum(factorial(digit) for digit in digitize(number)) == number))
