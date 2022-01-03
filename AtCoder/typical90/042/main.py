k = int(input())

if k % 9 != 0:
    print(0)
    exit()

dp = [0] * (k + 10)
dp[0] = 1
for i in range(k):
    for j in range(1, 10):
        dp[i + j] += dp[i]
        dp[i + j] %= 10 ** 9 + 7

print(dp[k])
