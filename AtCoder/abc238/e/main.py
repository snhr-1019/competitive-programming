from collections import deque

n, q = map(int, input().split())
edges = [[] for _ in range(n + 10)]
for i in range(q):
    l, r = map(int, input().split())
    r += 1
    edges[l].append(r)
    edges[r].append(l)

que = deque()
que.append(1)
visited = [False] * (n + 10)
visited[1] = True
while que:
    cur = que.popleft()

    if cur == n + 1:
        print("Yes")
        exit()

    for nxt in edges[cur]:
        if not visited[nxt]:
            que.append(nxt)
            visited[nxt] = True

print("No")
