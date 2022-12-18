from collections import deque

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

d = [-1] * n

ans = n * (n - 1) // 2 - m
for i in range(n):
    if d[i] != -1:
        continue
    que = deque()
    que.append(i)
    d[i] = 0
    c = [0] * 2
    c[0] = 1
    while que:
        cur = que.popleft()
        for nxt in edges[cur]:
            if d[nxt] == -1:
                que.append(nxt)
                d[nxt] = not d[cur]
                if d[nxt]:
                    c[1] += 1
                else:
                    c[0] += 1
            else:
                if d[nxt] == d[cur]:
                    # 最初から二部グラフでない
                    print(0)
                    exit()
    for i in range(2):
        ans -= c[i] * (c[i] - 1) // 2


print(ans)
