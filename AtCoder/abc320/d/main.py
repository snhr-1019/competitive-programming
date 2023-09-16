from collections import deque

n, m = map(int, input().split())

edges = [[] for _ in range(n)]

for _ in range(m):
    a, b, dx, dy = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, dx, dy))
    edges[b].append((a, -dx, -dy))

visited = [False] * n
visited[0] = True
pos = [[0, 0] for _ in range(n)]

que = deque()
que.append(0)

while que:
    cur = que.popleft()
    for nxt, dx, dy in edges[cur]:
        if visited[nxt]:
            continue

        visited[nxt] = True
        pos[nxt][0] = pos[cur][0] + dx
        pos[nxt][1] = pos[cur][1] + dy
        que.append(nxt)

for i in range(n):
    if visited[i]:
        print(pos[i][0], pos[i][1])
    else:
        print('undecidable ')
