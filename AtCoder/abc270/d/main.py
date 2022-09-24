from bisect import bisect_right

n, k = map(int, input().split())
a = list(map(int, input().split()))
sa = set(a)
ans = 0
while n > 0:
    t = bisect_right(a, n) - 1
    ans += a[t]
    n -= a[t]

    if n <= 0:
        break

    ao = bisect_right(a, n) - 1
    if n - a[ao] in sa:
        ao -= 1
    n -= a[ao]
print(ans)
