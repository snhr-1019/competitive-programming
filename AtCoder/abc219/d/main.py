N = int(input())
X, Y = map(int, input().split())
INF = 10 ** 18
dp = [[[INF for _ in range(Y + 1)] for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
# 配るDP
for i in range(N):
    a, b = map(int, input().split())
    for j in range(X + 1):
        for k in range(Y + 1):
            # i番目の弁当を買う場合
            # 右辺：既に別ルートで個数を確保できてる方法がある場合はそれと比較して弁当の個数が少ない方を採用
            dp[i + 1][min(a + j, X)][min(b + k, Y)] = min(dp[i + 1][min(a + j, X)][min(b + k, Y)], dp[i][j][k] + 1)
            # i番目の弁当を買わない場合
            # 右辺は同上
            dp[i + 1][j][k] = min(dp[i][j][k], dp[i + 1][j][k])

if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
