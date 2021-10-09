N = int(input())
a = list(map(int, input().split()))
b = list(map(lambda x: int(x) + 1, input().split()))
MOD = 998244353
dp = [[0] * 3010 for _ in range(N)]

for j in range(a[0], b[0]):
    dp[0][j] += 1

for i in range(N - 1):
    for j in range(3010):
        for k in range(max(j, a[i + 1]), b[i + 1]):
            # print(i, j, k)
            dp[i + 1][k] += dp[i][j]
            dp[i + 1][k] %= MOD

ans = 0
for x in dp[N - 1]:
    ans += x
    ans %= MOD
print(ans)
