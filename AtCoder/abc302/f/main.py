from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n + m)]
for i in range(n):
    ai = int(input())
    si = list(map(int, input().split()))
    for s in si:
        s -= 1
        edges[s].append(m + i)
        edges[m + i].append(s)

INF = 10 ** 9
que = deque()
que.append(0)
dist = [INF] * (n + m)
dist[0] = 0

while que:
    cur = que.popleft()
    for nxt in edges[cur]:
        if dist[nxt] != INF:
            continue

        dist[nxt] = dist[cur] + 1
        que.append(nxt)

ans = dist[m - 1]
if ans == INF:
    print(-1)
else:
    print((ans - 2) // 2)
