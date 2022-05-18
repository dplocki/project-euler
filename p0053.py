# https://projecteuler.net/problem=53

result = 0
line = [1]
for n in range(1, 101):
    current_line = [1]

    for left, right in zip(line, line[1:]):
        current_line.append(left + right)

    current_line.append(1)
    line = current_line

    result += sum(1 for value in line if value > 1_000_000)

print(result)
