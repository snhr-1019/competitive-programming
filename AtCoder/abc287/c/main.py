from collections import deque

n, m = map(int, input().split())

cnt = [0] * n

# 辺の数が頂点数-1でなければNG
if m != n - 1:
    print("No")
    exit()

edges = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

# 次数が2より大きい頂点があればNG
for i in range(n):
    if len(edges[i]) > 2:
        print("No")
        exit()

# 連携成分が2つ以上あったらNG
que = deque()
que.append(0)
visited = [False] * n
visited[0] = True
while que:
    cur = que.pop()

    for nxt in edges[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            que.append(nxt)

for i in range(n):
    if not visited[i]:
        print("No")
        exit()

print("Yes")