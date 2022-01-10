n, q = map(int, input().split())
a = list(map(int, input().split()))
d = [0] * n

inc = 0
for i in range(n - 1):
    d[i] = a[i + 1] - a[i]
    inc += abs(d[i])

for i in range(q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1
    l_before = d[l - 1]
    r_before = d[r]
    if l > 0:
        d[l - 1] += v
    if r < n - 1:
        d[r] -= v
    inc += abs(d[l - 1]) - abs(l_before)
    inc += abs(d[r]) - abs(r_before)
    print(inc)
