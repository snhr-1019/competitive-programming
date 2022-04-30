def solve():
    n, k = map(int, input().split())
    E = list(map(int, input().split()))

    sum_E = sum(E)

    if set(E) == {0}:
        return "1"
    if sum_E == 0:
        return "IMPOSSIBLE"
    x = (sum(map(lambda x: x ** 2, E)) - sum_E ** 2) / (2 * sum_E)
    if int(x) == x:
        return str(int(x))
    else:
        return "IMPOSSIBLE"


T = int(input())

for t in range(T):
    ans = solve()
    print(f'Case #{t + 1}: {ans}')
