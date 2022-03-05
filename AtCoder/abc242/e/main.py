t = int(input())

A = ord('A')
M = 998244353


def solve():
    n = int(input())
    s = list(map(ord, list(input())))
    kaibun = [0] * n
    kaibun[0] = s[0]
    kaibun[-1] = s[0]
    k = (n + 1) // 2
    dp = [0] * k
    dp[0] = s[0] - A
    for i in range(1, k):
        dp[i] += dp[i - 1] * 26
        dp[i] %= M
        dp[i] += s[i] - A
        dp[i] %= M
        kaibun[i] = s[i]
        kaibun[-i - 1] = s[i]
    ans = dp[k - 1]
    # print(kaibun)
    # print(s)
    if kaibun <= s:
        ans += 1
    print(ans % M)


for i in range(t):
    solve()
