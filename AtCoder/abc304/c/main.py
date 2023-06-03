from collections import deque


def euclid_dist2(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2)


n, d = map(int, input().split())
x = []
y = []
edge = [[] for _ in range(n)]

for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

for i in range(n - 1):
    for j in range(i + 1, n):
        dd = euclid_dist2(x[i], y[i], x[j], y[j])
        if dd <= d ** 2:
            edge[i].append(j)
            edge[j].append(i)

que = deque()
que.append(0)
virus = [False] * n
virus[0] = True

while que:
    cur = que.popleft()
    for nxt in edge[cur]:
        if virus[nxt]:
            continue
        virus[nxt] = True
        que.append(nxt)

for v in virus:
    if v:
        print("Yes")
    else:
        print("No")
