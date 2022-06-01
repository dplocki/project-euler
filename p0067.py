# https://projecteuler.net/problem=67

from typing import Iterator, List

def load_file(file_name: str) -> Iterator[List[int]]:
    with open(file_name, 'r') as file:
        return file.readlines()

def parse(lines: Iterator[str]) -> Iterator[List[int]]:
    yield from (list(map(int, line.split())) for line in lines)

def find_maximum_path(triangle: List[List[int]]) -> int:
    previous_line = {}
    for line in triangle[::-1][:-1]:
        current_line = [number + previous_line.get(index, 0) for index, number in enumerate(line)]
        previous_line = {
            index:max(left, right) 
            for index, (left, right) in enumerate(zip(current_line, current_line[1:]))}

    return previous_line[0] + triangle[0][0]

assert find_maximum_path(list(parse('''3
7 4
2 4 6
8 5 9 3'''.splitlines()))) == 23

# The is taken from: https://projecteuler.net/project/resources/p067_triangle.txt
triangle = list(parse(load_file('p067_triangle.txt')))
print(find_maximum_path(triangle))
