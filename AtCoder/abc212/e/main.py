N, M, K = map(int, input().split())
paths = []
for i in range(M):
    paths.append(list(map(lambda x: int(x) - 1, input().split())))

dp = [[0] * N for i in range(K + 1)]
dp[0][0] = 1
for i in range(K):
    # 合計を先に計算し、後で不要な経路の数を引く
    s = sum(dp[i])

    # 同じノードの経路は引く
    for j in range(N):
        dp[i + 1][j] = s - dp[i][j]

    # 道がないところの経路数を引く
    for u, v in paths:
        dp[i + 1][u] -= dp[i][v]
        dp[i + 1][v] -= dp[i][u]

    for j in range(N):
        dp[i + 1][j] %= 998244353

print(dp[K][0])
