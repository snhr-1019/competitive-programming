n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-10 ** 20] * (m + 1) for _ in range(n)]

for i in range(n):
    dp[i][0] = 0

dp[0][0] = 0
dp[0][1] = a[0]

for i in range(1, n):
    for j in range(1, m + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + j * a[i], dp[i - 1][j])

print(dp[n - 1][m])
