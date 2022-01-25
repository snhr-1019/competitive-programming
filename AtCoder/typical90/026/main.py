from collections import deque

n = int(input())
edges = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

c = [-1] * (n + 1)
q = deque()

q.append(1)
c[1] = 0

while q:
    cur = q.popleft()
    for nxt in edges[cur]:
        if c[nxt] != -1:
            continue
        q.append(nxt)
        c[nxt] = not c[cur]

a = []
b = []
for i in range(1, n + 1):
    if c[i] == 0:
        a.append(i)
    else:
        b.append(i)
if len(a) >= n // 2:
    print(*a[:n // 2])
else:
    print(*b[:n // 2])
