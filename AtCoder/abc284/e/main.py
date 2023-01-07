import sys

sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)
visited = [False] * n
visited[0] = True
ans = 0


def dfs(cur):
    global ans
    ans += 1
    if ans >= 10 ** 6:
        ans = 10 ** 6
        return

    for nxt in edges[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            dfs(nxt)
            visited[nxt] = False


dfs(0)
print(ans)
