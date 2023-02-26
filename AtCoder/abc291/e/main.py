"""
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
"""

import sys

sys.setrecursionlimit(10 ** 9)

n, m = map(int, input().split())
forward_edges = [[] for _ in range(n)]
reverse_edges = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    forward_edges[x].append(y)
    reverse_edges[y].append(x)

INF = 10 ** 9
dist = [INF] * n
dist[0] = 0
max_dist = {'node': 0, 'dist': 0}


def dfs(cur, prev, rev=False):
    if rev:
        edges = reverse_edges
    else:
        edges = forward_edges
    for nxt in edges[cur]:
        if nxt == prev:
            continue
        dist[nxt] = max(dist[nxt], dist[cur] + 1)
        if max_dist['dist'] < dist[nxt]:
            max_dist['dist'] = dist[nxt]
            max_dist['node'] = nxt
        dfs(nxt, cur, rev)


dfs(0, -1)

dist = [INF] * n
node = max_dist['node']
dist[node] = 0
max_dist = {'node': node, 'dist': 0}
dfs(node, -1, True)

if max_dist['dist'] == n - 1:
    print("Yes")

    ans = [0] * n
    for i in range(n):
        ans[i] = n - dist[i]
    print(*ans)
else:
    print("No")
