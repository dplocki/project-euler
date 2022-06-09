from typing import List

def list_totients(limit: int) -> List[int]:
	result = list(range(limit + 1))

	for i in range(2, limit + 1):
		if result[i] == i:
			for j in range(i, limit + 1, i):
				result[j] -= result[j] // i

	return result

def count_fractions(limit):
    return sum(list_totients(limit)) -1

assert count_fractions(8) == 21
print(count_fractions(1_000_000))
