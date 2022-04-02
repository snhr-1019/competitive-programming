def solve():
    inks = [[] for _ in range(4)]
    for printer in range(3):
        ink = list(map(int, input().split()))
        for color in range(4):
            inks[color].append(ink[color])

    mins = list(map(min, inks))
    if sum(mins) < K:
        print("IMPOSSIBLE")
        return
    ans = mins[:]
    for color in range(4):
        ans[color] -= min(ans[color], sum(ans) - K)
    print(*ans)


K = 10 ** 6
T = int(input())

for t in range(T):
    print(f'Case #{t + 1}: ', end="")
    solve()
