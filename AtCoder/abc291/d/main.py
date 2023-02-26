n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
M = 998244353

dp = [[0] * 2 for _ in range(n)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(1, n):
    for j in range(2):
        if ab[i - 1][0] != ab[i][j]:
            dp[i][j] += dp[i - 1][0]
            dp[i][j] %= M

        if ab[i - 1][1] != ab[i][j]:
            dp[i][j] += dp[i - 1][1]
            dp[i][j] %= M

print(sum(dp[n - 1]) % M)
