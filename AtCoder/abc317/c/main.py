import sys

setrecursionlimit = sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())

edges = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append((b, c))
    edges[b].append((a, c))

ans = 0
visited = [False] * n


def dfs(cur, cost):
    global ans
    visited[cur] = True
    ans = max(ans, cost)

    for nxt, nc in edges[cur]:
        if not visited[nxt]:
            dfs(nxt, cost + nc)
    visited[cur] = False


for i in range(n):
    dfs(i, 0)
print(ans)
