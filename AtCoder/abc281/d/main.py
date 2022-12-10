n, k, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1] * d for _ in range(k + 1)]
dp[0][0] = 0
for i in range(n):
    ndp = [[-1] * d for _ in range(k + 1)]

    for j in range(k + 1):
        for l in range(d):
            if dp[j][l] == -1:
                continue
            # a[i]を使わない場合
            ndp[j][l] = max(ndp[j][l], dp[j][l])

            # a[i]を使う場合
            if j < k:
                nxt_l = (l + a[i]) % d
                ndp[j + 1][nxt_l] = max(ndp[j + 1][nxt_l], dp[j][l] + a[i])

    dp = ndp

print(dp[k][0])
