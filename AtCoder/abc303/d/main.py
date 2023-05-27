a, shift, caps = map(int, input().split())
s = input()

INF = 10 ** 18
dp = [[INF] * 2 for _ in range(len(s) + 1)]

dp[0][0] = 0

for i in range(len(s)):
    t = (s[i] == 'A')

    for j in range(2):
        for k in range(2):
            if k == t:
                cost = a
            else:
                cost = shift

            if j != k:
                cost += caps

            dp[i + 1][k] = min(dp[i + 1][k], dp[i][j] + cost)
print(min(dp[-1]))
