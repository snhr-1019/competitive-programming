n, m = map(int, input().split())

c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
prices = dict()
for i in range(m):
    prices[d[i]] = p[i + 1]
ans = 0
for i in range(n):
    if c[i] in prices.keys():
        ans += prices[c[i]]
    else:
        ans += p[0]
print(ans)
