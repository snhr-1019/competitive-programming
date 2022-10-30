n, m, k = map(int, input().split())

# dp[i][j] := ルーレットをi回回したときに、jのマスにいる確率
# ルーレットi回目
mod = 998244353
dp = [0] * (n + 1)
dp[0] = 1
minv = pow(m, mod - 2, mod)

for i in range(k):
    nxt_dp = [0] * (n + 1)
    nxt_dp[n] = dp[n]
    # sのマスから初めて
    for s in range(n):
        # 目がjだったとき
        for d in range(1, m + 1):
            if s + d <= n:
                # 折り返さない場合
                nxt_dp[s + d] += dp[s] * minv
                nxt_dp[s + d] %= mod
            else:
                # 折り返す場合
                nxt_dp[2 * n - (s + d)] += dp[s] * minv
                nxt_dp[2 * n - (s + d)] %= mod
    dp = nxt_dp

print(dp[n])
