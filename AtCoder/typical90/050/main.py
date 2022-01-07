n, l = map(int, input().split())
dp = [0] * (10 ** 6)
dp[0] = 1
MOD = 10 ** 9 + 7
for i in range(n):
    dp[i + 1] += dp[i]
    dp[i + 1] %= MOD

    dp[i + l] += dp[i]
    dp[i + l] %= MOD
print(dp[n])
