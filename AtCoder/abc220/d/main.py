N = int(input())
A = list(map(int, input().split()))
C = 998244353
dp = [[0] * 10 for i in range(N)]

dp[0][A[0]] = 1

for i in range(N - 1):
    for j in range(10):
        x = j
        y = A[i + 1]
        f = (x + y) % 10
        g = (x * y) % 10
        dp[i + 1][f] += dp[i][j]
        dp[i + 1][g] += dp[i][j]
        dp[i + 1][f] %= C
        dp[i + 1][g] %= C

for i in range(10):
    print(dp[N - 1][i])
