# https://projecteuler.net/problem=15

def lattice_paths(gird_size: int) -> int:
    solutions = { (gird_size + 1, gird_size + 1): 0 }

    for column in range(gird_size, 0, -1):
        solutions[gird_size + 1, column] = 1

    for row in range(gird_size, 0, -1):
        solutions[row, gird_size + 1] = 1

    for row in range(gird_size, 0, -1):
        for column in range(gird_size, 0, -1):
            solutions[row, column] = solutions[row + 1, column] + solutions[row, column + 1]

    return solutions[1, 1]

assert lattice_paths(2) == 6
print(lattice_paths(20))
