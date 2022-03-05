n = int(input())
M = 998244353

dp = [[0] * 9 for _ in range(n)]
for i in range(9):
    dp[0][i] = 1

for i in range(n - 1):
    for j in range(9):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= M
        if j != 0:
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= M
        if j != 8:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= M

ans = 0
for i in range(9):
    ans += dp[n - 1][i]
    ans %= M
print(ans)
