n = int(input())
a = list(map(int, input().split()))
INF = 10 ** 18

# 行動0を行わない場合
dp = [[0] * 2 for _ in range(n)]
ans = INF
dp[0][0] = 0
dp[0][1] = a[0]
for i in range(1, n):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i]

ans = dp[n - 1][1]

# 行動0を行う場合
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = INF
dp[0][1] = a[0]
for i in range(1, n):
    dp[i][0] = dp[i - 1][1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + a[i]

ans = min(ans, dp[n - 1][0], dp[n - 1][1])
print(ans)
