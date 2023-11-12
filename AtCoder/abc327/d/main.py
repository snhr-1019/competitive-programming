from collections import deque

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

edges = [[] for _ in range(n)]
for i in range(m):
    edges[a[i] - 1].append(b[i] - 1)
    edges[b[i] - 1].append(a[i] - 1)

val = [-1] * n

for i in range(n):
    if val[i] != -1:
        continue

    val[i] = 0
    que = deque()
    que.append(i)

    while que:
        cur = que.popleft()
        for nxt in edges[cur]:
            if val[nxt] == -1:
                val[nxt] = val[cur] ^ 1
                que.append(nxt)
            elif val[nxt] == val[cur]:
                print('No')
                exit()
print('Yes')