s = input()
n = len(s)
MOD = 998244353
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    if s[i] == '(':
        for j in range(n):
            dp[i + 1][j + 1] = dp[i][j]
    elif s[i] == ')':
        for j in range(1, n):
            dp[i + 1][j - 1] = dp[i][j]
    else:
        # '('にする場合
        for j in range(n):
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD
        # ')'にする場合
        for j in range(1, n):
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= MOD
print(dp[n][0] % MOD)
