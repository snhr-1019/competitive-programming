n, k = map(int, input().split())
a = list(map(int, input().split()))

r, s, ans = 0, 0, 0
for l in range(n):
    if l > 0:
        s -= a[l - 1]
    while r < n and s < k:
        s += a[r]
        r += 1
    print(l, r, s)
    ans += 1
print(ans)
