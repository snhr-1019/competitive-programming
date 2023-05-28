from collections import deque

n = int(input())

deg = [0] * n
edges = [[] for _ in range(n)]

types = [-1] * n
UNKNOWN = -1
PARENT = 0
CHILD = 1

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    deg[u] += 1
    deg[v] += 1
    edges[u].append(v)
    edges[v].append(u)

que = deque()

for i in range(n):
    if deg[i] == 1:
        types[i] = CHILD
        que.append((i, CHILD))
        break

while que:
    cur, prev = que.popleft()

    for nxt in edges[cur]:
        if types[nxt] != UNKNOWN:
            continue

        if types[cur] == PARENT:
            types[nxt] = CHILD
            que.append((nxt, PARENT))
        else:
            if prev == PARENT:
                types[nxt] = CHILD
                que.append((nxt, CHILD))
            else:
                types[nxt] = PARENT
                que.append((nxt, PARENT))

ans = []
for i in range(n):
    if types[i] == PARENT:
        ans.append(deg[i])
ans.sort()
print(*ans)
