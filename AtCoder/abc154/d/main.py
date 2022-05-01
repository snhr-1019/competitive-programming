n, k = map(int, input().split())
p = list(map(int, input().split()))
ev = list(map(lambda x: (x + 1) / 2, p))
s = sum(ev[:k])
ans = s
for i in range(k, n):
    s += ev[i]
    s -= ev[i - k]
    ans = max(ans, s)
print(ans)
