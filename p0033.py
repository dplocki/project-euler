# https://projecteuler.net/problem=33

from math import gcd

def find_cancelable_fractions():
    for numerator in range(10, 100):
        for denominator in range(10, 100):
            if numerator >= denominator:
                continue

            divider = gcd(denominator, numerator)
            if divider == 1:
                continue

            if numerator % 10 == 0:
                continue

            if ((numerator % 10 != denominator % 10) \
                and (numerator // 10 != denominator // 10) \
                and (numerator // 10 != denominator % 10) \
                and (numerator % 10 != denominator // 10)):
                continue

            value_of_base_denominator = denominator // divider
            value_of_base_numerator = numerator // divider

            cancel_fraction_numerator, cancel_fraction_denominator = 0, 0
            if numerator % 10 == denominator % 10:
                cancel_fraction_numerator, cancel_fraction_denominator = numerator // 10, denominator // 10
            elif numerator // 10 == denominator // 10:
                cancel_fraction_numerator, cancel_fraction_denominator = numerator % 10, denominator % 10
            elif numerator // 10 == denominator % 10:
                cancel_fraction_numerator, cancel_fraction_denominator = numerator % 10, denominator // 10
            elif numerator % 10 == denominator // 10:
                cancel_fraction_numerator, cancel_fraction_denominator = numerator // 10, denominator % 10

            if cancel_fraction_numerator == 0 or cancel_fraction_denominator == 0:
                continue

            the_cancel_divider = gcd(cancel_fraction_denominator, cancel_fraction_numerator)
            value_of_cancel_denominator = cancel_fraction_denominator // the_cancel_divider
            value_of_cancel_numerator = cancel_fraction_numerator // the_cancel_divider

            if value_of_base_denominator != value_of_cancel_denominator \
                or value_of_base_numerator != value_of_cancel_numerator:
                continue

            yield numerator, denominator


result_numerator = 1
result_denominator = 1

for numerator, denominator in find_cancelable_fractions():
    result_numerator *= numerator
    result_denominator *= denominator

print(result_denominator // gcd(result_numerator, result_denominator))
