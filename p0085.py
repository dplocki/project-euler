# https://projecteuler.net/problem=85

def get_rectangles_count(width: int, height: int) -> int:
    result = 0
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            result += (width - w + 1) * (height - h + 1)

    return result

assert get_rectangles_count(3, 2) == 18

results = {
    abs(2_000_000 - get_rectangles_count(w, h)): w * h
    for w in range(1, 100)
    for h in range(1, 100)
}

print('Solution:', results[sorted(results.keys())[0]])
