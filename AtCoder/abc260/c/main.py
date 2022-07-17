n, x, y = map(int, input().split())
dp = [[0] * 2 for _ in range(n + 1)]
dp[n][0] = 1

# 操作A：レベル n の赤い宝石 (n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n の青い宝石 X 個」に変換する。
# 操作B：レベル n の青い宝石 (n は 2 以上) を「レベル n−1 の赤い宝石 1 個と、レベル n−1 の青い宝石 Y 個」に変換する。
for i in reversed(range(2, n + 1)):
    # 操作A
    dp[i][1] += dp[i][0] * x
    dp[i - 1][0] += dp[i][0]

    # 操作B
    dp[i - 1][0] += dp[i][1]
    dp[i - 1][1] += dp[i][1] * y

print(dp[1][1])
