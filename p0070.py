# https://projecteuler.net/problem=70

from typing import List

def list_totients(limit: int) -> List[int]:
	result = list(range(limit + 1))

	for i in range(2, limit + 1):
		if result[i] == i:
			for j in range(i, limit + 1, i):
				result[j] -= result[j] // i

	return result

best_n = 1
best_phi = 0
phi_values = list_totients(10_000_000)

for n in range(2, len(phi_values)):
	phi_n = phi_values[n]
	if n * best_phi < best_n * phi_n and ''.join(sorted(str(n))) == ''.join(sorted(str(phi_n))):
		best_phi = phi_n
		best_n = n

print(best_n)
