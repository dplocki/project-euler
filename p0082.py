# https://projecteuler.net/problem=82
from queue import PriorityQueue
from typing import Generator, List, Tuple

def load_input(file_name: str) -> Generator[Tuple[int, ...], None, None]:
    with open(file_name, 'r') as file:
        for line in file.readlines():
            yield tuple(map(int, line.split(',')))

def solution(task_input: List[Tuple[int, ...]]):
    table = {
        (column_index, row_index): element
        for row_index, row in enumerate(task_input)
        for column_index, element in enumerate(row)}

    last_row = len(task_input) - 1
    last_column = len(task_input[0]) - 1

    def neighbors(column_index: int, row_index: int) -> Generator[Tuple[int, int], None, None]:
        if column_index > 0 and row_index > 0:
            yield column_index, row_index - 1

        if column_index > 0 and row_index < last_row:
            yield column_index, row_index + 1

        if column_index >= 0:
            yield column_index + 1, row_index
        
    def solution_from(start_row_index: int) -> int:
        to_check = PriorityQueue()
        to_check.put((table[0, start_row_index], (0, start_row_index)))
        cost_so_far = {(0, start_row_index): table[0, start_row_index]}

        while not to_check.empty():
            _, (column_index, row_index) = to_check.get()

            if column_index == last_column:
                return cost_so_far[column_index, row_index]

            for new_point in neighbors(column_index, row_index):
                new_cost = cost_so_far[column_index, row_index] + table[new_point]

                if new_point not in cost_so_far or new_cost < cost_so_far[new_point]:
                    cost_so_far[new_point] = new_cost
                    to_check.put((new_cost, new_point))

        raise Exception('Unexpected')

    return min(solution_from(start_row_index) for start_row_index in range(len(task_input)))

assert solution([
    (131, 673, 234, 103, 18),
    (201, 96, 342, 965, 150),
    (630, 803, 746, 422, 111),
    (537, 699, 497, 121, 956),
    (805, 732, 524, 37, 331)]) == 994

print(solution(list(load_input('matrix.txt'))))
