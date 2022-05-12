# https://projecteuler.net/problem=42

from itertools import takewhile

BASE_LETTER_VALUE = ord('A') - 1

def load_words(file_name: str) -> list[str]:
    with open(file_name) as file:
        file_content = file.read()
        words = sorted(file_content.split(','))
        for word in words:
            yield word[1:-1]

def triangle_numbers() -> int:
    n = 1
    while True:
        yield n * (n + 1) // 2
        n += 1

def word_value(word: str) -> int:
    return sum((ord(character) - BASE_LETTER_VALUE) for character in word)

assert word_value('SKY') == 55

words_values = [word_value(word) for word in load_words('p042_words.txt')]
max_word_value = max(words_values)
triangle_numbers_values = set(takewhile(lambda x: x < max_word_value, triangle_numbers()))

print(sum(1 for word_value in words_values if word_value in triangle_numbers_values))
