# https://projecteuler.net/problem=59

from typing import List

ASCII_LOWERCASE_A = ord('a')
ASCII_LOWERCASE_Z = ord('z')

FREQUENCY_CHARACTERS_WEIGHT = {
	ord(' '): 13,

	ord('e'): 12,
	ord('t'): 11,
	ord('a'): 10,
	ord('o'): 9,
	ord('i'): 8,
	ord('n'): 7,
	ord('s'): 6,
	ord('h'): 5,
	ord('r'): 4,
	ord('d'): 3,
	ord('l'): 2,
	ord('u'): 1,

	ord('E'): 12,
	ord('T'): 11,
	ord('A'): 10,
	ord('O'): 9,
	ord('I'): 8,
	ord('N'): 7,
	ord('S'): 6,
	ord('H'): 5,
	ord('R'): 4,
	ord('D'): 3,
	ord('L'): 2,
	ord('U'): 1,
}

def load_file(file_name: str) -> List[int]:
    with open(file_name, 'r') as file:
        file_content = file.read()
        return (int(token) for token in file_content.split(','))

def break_single_letter(letters: List[int]) -> List[int]:
    result = None
    frequent_character_result = 0

    for letter_in_key in range(ASCII_LOWERCASE_A, ASCII_LOWERCASE_Z + 1):
        current_result = [letter ^ letter_in_key for letter in letters]
        current_frequent_character_result = sum(FREQUENCY_CHARACTERS_WEIGHT.get(letter, 0) for letter in current_result)

        if current_frequent_character_result > frequent_character_result:
            result = current_result
            frequent_character_result = current_frequent_character_result

    return result

# File is teken from: https://projecteuler.net/project/resources/p059_cipher.txt
cypher_text = list(load_file('p059_cipher.txt'))

encode_by_first_key_letter = break_single_letter(cypher_text[0::3])
encode_by_second_key_letter = break_single_letter(cypher_text[1::3])
encode_by_third_key_letter = break_single_letter(cypher_text[2::3])

print(sum(encode_by_first_key_letter) + sum(encode_by_second_key_letter) + sum(encode_by_third_key_letter))
