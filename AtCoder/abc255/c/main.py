from decimal import Decimal, ROUND_HALF_UP

x, a, d, n = map(int, input().split())
l = a
r = a + d * (n - 1)
mn = min(l, r)
mx = max(l, r)
if mx < x:
    print(x - mx)
elif x < mn:
    print(mn - x)
elif d == 0:
    print(abs(x - a))
else:
    t = x - a
    k = int((t + (d / 2)) // d)

    ans = 10 ** 10
    for i in range(max(0, k - 10), min(k + 10, n)):
        tmp = abs(x - (a + i * d))
        ans = min(ans, tmp)
    print(ans)
