n = int(input())
d = len(str(n))
M = 998244353
ans = 0
for i in range(d):
    s = 10 ** i
    e = min(n, 10 ** (i + 1) - 1)
    ans += (1 + (e - s + 1)) * (e - s + 1) // 2
    ans %= M
print(ans)
