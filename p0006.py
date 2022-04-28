# https://projecteuler.net/problem=6

sum_of_squars = 0
sum_of_numbers = 0

for i in range(1, 101):
    sum_of_squars += i * i
    sum_of_numbers += i

print(sum_of_numbers ** 2 - sum_of_squars)
