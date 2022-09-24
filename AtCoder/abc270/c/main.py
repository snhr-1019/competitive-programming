from collections import deque

n, x, y = map(int, input().split())

edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

q = deque()
q.append(x)
prev = [-1] * (n + 1)
prev[x] = 0

while q:
    cur = q.pop()
    for nxt in edges[cur]:
        if prev[nxt] != -1:
            continue
        q.append(nxt)
        prev[nxt] = cur
        if nxt == y:
            break

ans = [y]
cur = y
while prev[cur] != 0:
    cur = prev[cur]
    ans.append(cur)
print(*reversed(ans))
