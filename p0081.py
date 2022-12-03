# https://projecteuler.net/problem=81
from typing import Generator, Tuple

def load_input() -> Generator[Tuple[int, ...], None, None]:
    with open('matrix.txt', 'r') as file:
        for line in file.readlines():
            yield tuple(map(int, line.split(',')))

def solution() -> int:
    line_provider = load_input()
    first_row = next(line_provider)

    result_line = [ first_row[0] ]
    for number in first_row[1:]:
        result_line.append(number + result_line[-1])

    for numbers in line_provider:
        for index, number in enumerate(numbers):
            if index > 0 and result_line[index] > result_line[index - 1]:
                result_line[index] = number + result_line[index - 1]
            else:
                result_line[index] = number + result_line[index]

    return result_line[-1]

print(solution())
