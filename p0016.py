# https://projecteuler.net/problem=16

def power_digit_sum(number: int):
    return sum(int(digit) for digit in str(number))
   
assert power_digit_sum(2 ** 15) == 26
print(power_digit_sum(2 ** 1000))
