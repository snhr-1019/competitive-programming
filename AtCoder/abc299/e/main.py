from collections import deque

n, m = map(int, input().split())

edges = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

k = int(input())
pd = []
for _ in range(k):
    p, d = map(int, input().split())
    p -= 1
    pd.append((p, d))

dist = [[-1] * n for _ in range(n)]


def dfs(s):
    dist[s][s] = 0
    que = deque([s])
    while que:
        cur = que.popleft()
        for nxt in edges[cur]:
            if dist[s][nxt] == -1:
                dist[s][nxt] = dist[s][cur] + 1
                que.append(nxt)


for s in range(n):
    dfs(s)

color = [1] * n

for p, d in pd:
    for i in range(n):
        if dist[p][i] < d:
            color[i] = 0

for p, d in pd:
    mn = n + 1
    for to in range(n):
        if color[to] == 1:
            mn = min(mn, dist[p][to])
    if mn != d:
        print("No")
        exit()

print("Yes")
print(*color, sep='')
