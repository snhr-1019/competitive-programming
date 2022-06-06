from collections import deque

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def solve(x, k):
    ans = x
    que = deque()
    que.append(x)
    visited = [False] * (n + 1)
    visited[x] = True
    while que and k > 0:
        cur = que.popleft()
        for nxt in edges[cur]:
            if visited[nxt]:
                continue
            que.append(nxt)
            visited[nxt] = True
            ans += nxt
        k -= 1
    print(ans)


q = int(input())
for i in range(q):
    x, k = map(int, input().split())
    solve(x, k)
