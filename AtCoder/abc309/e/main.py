from collections import deque
from bisect import bisect_right

n, m = map(int, input().split())
c = [[] for _ in range(n)]

p = list(map(int, input().split()))
for i in range(n - 1):
    c[p[i] - 1].append(i + 1)

x = [0] * m
y = [0] * m
for i in range(m):
    xi, yi = map(int, input().split())
    xi -= 1
    x[i] = xi
    y[i] = yi

d = [-1] * n
d[0] = 0

que = deque([0])

while que:
    cur = que.popleft()
    for nxt in c[cur]:
        d[nxt] = d[cur] + 1
        que.append(nxt)

ans = 0
for i in range(n):
    t = bisect_right(x, i)
    for j in range(t - 1, -1, -1):
        ins = x[j]
        if d[ins] - d[i] <= y[j]:
            print(i, ins)
            ans += 1
            break
print(ans)
