n, m = map(int, input().split())

p = [0] + list(map(int, input().split()))
for i in range(n):
    p[i] -= 1

dp = [-1] * n

x = [0] * m
y = [0] * m
for i in range(m):
    xi, yi = map(int, input().split())
    xi -= 1
    dp[xi] = max(dp[xi], yi)

for i in range(1, n):
    dp[i] = max(dp[i], dp[p[i]] - 1)

ans = 0
for i in range(n):
    ans += (dp[i] >= 0)
print(ans)
