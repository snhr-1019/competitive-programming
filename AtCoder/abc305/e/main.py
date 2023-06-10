from collections import deque

n, m, k = map(int, input().split())

edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dp = [-1] * n
que = deque()
for _ in range(k):
    p, h = map(int, input().split())
    p -= 1
    dp[p] = h
    que.append((p, h))

while que:
    cur, h = que.popleft()
    h -= 1
    for nxt in edges[cur]:
        if dp[nxt] < h:
            dp[nxt] = h
            que.append((nxt, h))

ans = []
for i in range(n):
    if dp[i] >= 0:
        ans.append(i + 1)
print(len(ans))
print(*ans)
