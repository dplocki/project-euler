# https://projecteuler.net/problem=22

ZERO_LETTER_VALUE = ord('A') - 1

def load_names(file_name: str) -> list[str]:
    with open(file_name) as file:
        file_content = file.read()
        names = sorted(file_content.split(','))
        for name in names:
            yield name[1:-1]

def name_score(name: str) -> int:
    return sum(
        ord(character) - ZERO_LETTER_VALUE
        for character in name)

assert name_score('COLIN') == 53

# The names file is avaible on link: https://projecteuler.net/project/resources/p022_names.txt
print(sum((index + 1) * name_score(name) for index, name in enumerate(sorted(load_names('p022_names.txt')))))
