l, r = map(int, input().split())
ld = len(str(l))
rd = len(str(r))
ans = 0
for d in range(ld, rd + 1):
    s = max(l, 10 ** (d - 1))
    e = min(r, 10 ** d - 1)
    ans += (s + e) * (e - s + 1) * d // 2
    ans %= 10 ** 9 + 7
print(ans)
