N, K = map(int, input().split())
dp = [0] * N
dp[0] = 1
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
        start = max(0, i-R[j])
        end = max(0, i-L[j])
        cnt += sum(dp[start:end]) % mod
        cnt %= mod
        # for k in range(L[j], R[j] + 1):
        #     if i - k >= 0:
        #         cnt += dp[i - k]
        #         cnt %= 998244353
        #     else:
        #         continue
    dp[i] = cnt

print(dp[N - 1])
