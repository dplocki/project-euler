# https://projecteuler.net/problem=36

def is_palindrome(n: str) -> bool:
    length = len(n) // 2
    return n[0:length] == n[::-1][0:length]

assert is_palindrome('585') == True
assert is_palindrome('1001001001') == True

print(sum(number
    for number in range(1_000_000)
    if is_palindrome(str(number)) and is_palindrome(format(number, 'b'))))
