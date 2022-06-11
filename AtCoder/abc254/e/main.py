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
    que.append((x, 0))
    visited = set()
    visited.add(x)
    while que:
        cur, cur_d = que.popleft()
        if cur_d >= k:
            continue
        for nxt in edges[cur]:
            if nxt not in visited:
                que.append((nxt, cur_d + 1))
                visited.add(nxt)
                ans += nxt
    print(ans)


q = int(input())
for i in range(q):
    x, k = map(int, input().split())
    solve(x, k)
