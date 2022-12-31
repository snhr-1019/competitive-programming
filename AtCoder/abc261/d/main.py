from collections import defaultdict

n, m = map(int, input().split())
x = [0] + list(map(int, input().split()))
cy = defaultdict(int)
for _ in range(m):
    c, y = map(int, input().split())
    cy[c] = y
dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

# 配るDP
# i+1回目のトスをする直前を考える
for i in range(n):
    # i回目をトスする前にカウンタがjである場合
    for j in range(n + 1):
        if dp[i][j] == -1:
            continue

        # 表が出たとき
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i + 1] + cy[j + 1])

        # 裏が出たとき
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
print(max(dp[-1]))
