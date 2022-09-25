N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = 1
for n in range(2, N + 1):
    for i in range(K):
        if n - a[i] < 0:
            continue
        dp[n] = max(dp[n], n - dp[n - a[i]])

print(dp[N])
