n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))

INF = n + 1
dp = [[[INF] * 2 for _ in range(m + 1)] for __ in range(n + 1)]
dp[0][0][1] = 0

# aのi番目の要素に着目
for i in range(1, n + 1):
    # 作りたい部分和をjとする
    for j in range(m + 1):
        # i番目を使わない場合
        dp[i][j][0] = min(dp[i - 1][j][0], dp[i - 1][j][1] + 1)

        # i番目を使う場合
        if j - a[i] >= 0:
            dp[i][j][1] = min(dp[i - 1][j - a[i]][0], dp[i - 1][j - a[i]][1])

for i in range(1, m + 1):
    t = min(dp[n][i])
    if t == INF:
        print(-1)
    else:
        print(min(dp[n][i]))
