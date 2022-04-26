# https://projecteuler.net/problem=7

def nth_prime(n: int) -> int:
    primes = { 2 }
    number = 3

    while True:
        if all(number % prime != 0 for prime in primes):
            if len(primes) == n - 1:
                return number

            primes.add(number)
        
        number += 2


assert nth_prime(6) == 13
print(nth_prime(10001))
