from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
indeg = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges[x].append(y)
    indeg[y] += 1

que = deque()
for i in range(n):
    if indeg[i] == 0:
        que.append(i)

ans = [-1] * n
cnt = 0
while que:
    if len(que) > 1:
        print("No")
        exit()
    cur = que.popleft()
    cnt += 1
    ans[cur] = cnt
    for nxt in edges[cur]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            que.append(nxt)

print("Yes")
print(*ans)
