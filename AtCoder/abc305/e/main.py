from heapq import heappush, heappop

n, m, k = map(int, input().split())

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

visited = [-1] * n
hq = []

for _ in range(k):
    p, h = map(int, input().split())
    p -= 1
    heappush(hq, (-h, p))
    visited[p] = h

while hq:
    h, cur = heappop(hq)
    h = -h

    if visited[cur] != -1 and visited[cur] > h:
        continue
    if h == 0:
        continue

    for nxt in edges[cur]:
        if visited[nxt] == -1 or visited[nxt] < h - 1:
            visited[nxt] = h - 1
            heappush(hq, (-(h - 1), nxt))

ans = []
for i in range(n):
    if visited[i] >= 0:
        ans.append(i + 1)
print(len(ans))
print(*ans)
