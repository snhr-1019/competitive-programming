n, k = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

max_ds = [0] * (n - 1)

min_ds = [0] * n
for i in range(n):
    min_d = 10 ** 10
    for ai in A:
        a = xy[ai]
        d = (abs(a[0] - xy[i][0]) ** 2 + abs(a[1] - xy[i][1]) ** 2) ** 0.5
        min_d = min(min_d, d)
    min_ds[i] = min_d
print(max(min_ds))
