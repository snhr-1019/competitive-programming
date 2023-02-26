from collections import deque

n, m = map(int, input().split())
forward_edges = [[] for _ in range(n)]
reverse_edges = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    forward_edges[x].append(y)
    reverse_edges[y].append(x)


def dfs(start, rev=False):
    dist = [-1] * n
    dist[start] = 0
    max_dist = {'node': start, 'dist': 0}

    if rev:
        edges = reverse_edges
    else:
        edges = forward_edges

    stack = deque()
    stack.append((start, -1))
    while stack:
        cur, prev = stack.pop()
        for nxt in edges[cur]:
            if nxt == prev:
                continue
            dist[nxt] = dist[cur] + 1
            if max_dist['dist'] < dist[nxt]:
                max_dist['dist'] = dist[nxt]
                max_dist['node'] = nxt
            stack.append((nxt, cur))
    return max_dist, dist


max_dist, dist = dfs(0, False)
max_dist, dist = dfs(max_dist['node'], True)

if max_dist['dist'] == n - 1:
    print("Yes")

    ans = [0] * n
    for i in range(n):
        ans[i] = n - dist[i]
    print(*ans)
else:
    print("No")
