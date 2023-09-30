n, k, p = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

p += 1
INF = 10 ** 18
dp = [[INF] * p ** k for _ in range(n + 1)]

dp[0][0] = 0


def add(x, y):
    ret = [0] * k
    for i in range(k):
        xi = x % p
        x //= p
        ret[i] = min(xi + y[i], p - 1)
    return sum([ret[i] * p ** i for i in range(k)])


for i in range(n):
    for j in range(p ** k):
        if dp[i][j] == INF:
            continue
        # i番目を開発しない場合
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

        # i番目を開発する場合
        new_j = add(j, a[i][1:])
        dp[i + 1][new_j] = min(dp[i + 1][new_j], dp[i][j] + a[i][0])

if dp[n][-1] == INF:
    print(-1)
else:
    print(dp[n][-1])
