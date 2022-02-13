n, m = map(int, input().split())
INF = 10 ** 9

edges = [[INF] * n for _ in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a][b] = c

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i][j] = 0 if i == j else edges[i][j]

ans = 0
for k in range(n):
    for s in range(n):
        for t in range(n):
            dp[s][t] = min(dp[s][t], dp[s][k] + dp[k][t])
            if dp[s][t] < INF:
                ans += dp[s][t]
print(ans)
