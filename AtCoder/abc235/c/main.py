from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))
x = [0] * q
k = [0] * q
x_set = set()
for i in range(q):
    t, s = map(int, input().split())
    x[i] = t
    k[i] = s
    x_set.add(t)

dd = defaultdict(list)

for i in range(n):
    dd[a[i]].append(i)

for i in range(q):
    xi = x[i]
    ki = k[i]
    if len(dd[xi]) < ki:
        print(-1)
    else:
        print(dd[xi][ki - 1] + 1)
