import sys

sys.setrecursionlimit(10 ** 7)

n = int(input())
edges = [[] for _ in range(n)]

for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

l = 0
ans = [[-1, -1] for _ in range(n)]
visited = [False] * n
visited[0] = True


def dfs(cur):
    global l
    global ans

    mx = -1
    mn = 10 ** 9
    for nxt in edges[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        ret = dfs(nxt)
        mn = min(mn, ret[0])
        mx = max(mx, ret[1])

    if mx == -1:
        # 末端だったとき
        l += 1
        ans[cur] = [l, l]
        return [l, l]
    else:
        ans[cur] = [mn, mx]
        return [mn, mx]


dfs(0)
for i in range(n):
    print(*ans[i])
