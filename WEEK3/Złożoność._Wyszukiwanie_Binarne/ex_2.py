def solve_equation(i, j):
    left = 1
    right = j
    while left <= right:
        mid = (left + right) // 2
        candidate = mid**3 + i * mid
        if candidate == j:
            return mid
        elif candidate < j:
            left = mid + 1
        else:
            right = mid - 1
    return None


z = int(input())

for _ in range(z):
    p, q = map(int, input().split())
    result = solve_equation(p, q)
    if result is not None:
        print(result)
    else:
        print("NIE")
