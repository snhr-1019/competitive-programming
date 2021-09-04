import bisect

L, Q = map(int, input().split())
h = [0, L]

for i in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        bisect.insort(h, x)
    else:
        p = bisect.bisect(h, x)
        print(h[p] - h[p - 1])
