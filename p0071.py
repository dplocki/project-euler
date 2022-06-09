best_numerator = 0
best_denumerator = 1

for candidate_denumerator in range(1, 1_000_000):
    if candidate_denumerator % 7 == 0:
        continue
    
    candidate_numerator = 3*candidate_denumerator // 7
    
    if best_denumerator * candidate_numerator > candidate_denumerator * best_numerator:
        best_numerator = candidate_numerator
        best_denumerator = candidate_denumerator
        
print(best_numerator)
