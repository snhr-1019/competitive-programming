def solve():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    ans = 0
    for i in range(n):
        if ans + 1 <= s[i]:
            ans += 1
    print(ans)

T = int(input())

for t in range(T):
    print(f'Case #{t + 1}: ', end="")
    solve()
