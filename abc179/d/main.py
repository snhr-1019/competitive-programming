N, K = map(int, input().split())
dp = [0] * N
dp[0] = 1
dp_sum = [0] * N
dp_sum[0] = 1
L = [0] * K
R = [0] * K
mod = 998244353

for i in range(K):
    l, r = map(int, input().split())
    L[i] = l
    R[i] = r

for i in range(1, N):
    # マスiにたどり着くためのパターン数を数える
    cnt = 0
    for j in range(K):
        start = max(0, i - R[j])
        end = i - L[j]
        cnt += (dp_sum[end] - dp_sum[start - 1]) % mod
        cnt %= mod
    dp[i] = cnt
    dp_sum[i] = dp_sum[i - 1] + cnt

print(dp[N - 1])
