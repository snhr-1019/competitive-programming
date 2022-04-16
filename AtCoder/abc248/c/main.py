n, m, k = map(int, input().split())
MOD = 998244353
dp = [0] * (k + 1)
for i in range(1, m + 1):
    dp[i] = 1

for i in range(n - 1):
    dp_nxt = [0] * (k + 1)
    for j in range(1, (k + 1)):
        for d in range(1, m + 1):
            if j + d <= k:
                dp_nxt[j + d] += dp[j]
                dp_nxt[j + d] %= MOD
    dp = dp_nxt

print(sum(dp) % MOD)
