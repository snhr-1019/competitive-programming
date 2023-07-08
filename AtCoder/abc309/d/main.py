from collections import deque

n1, n2, m = map(int, input().split())
edges = [[] for _ in range(n1 + n2)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

def bfs(s, n):
    que = deque([s])
    d = [-1] * n
    d[s] = 0
    mx = 0
    while que:
        cur = que.popleft()
        for nxt in edges[cur]:
            if d[nxt] != -1:
                continue
            d[nxt] = d[cur] + 1
            mx = d[nxt]
            que.append(nxt)
    return mx

m1 = bfs(0, n1)
m2 = bfs(n1 + n2 - 1, n1 + n2)

print(m1 + m2 + 1)
