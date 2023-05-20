from collections import deque

n, m = map(int, input().split())

s = []
starts = set()
goals = set()

t = [set() for _ in range(m + 1)]

for i in range(n):
    a = int(input())
    si = set(map(int, input().split()))
    s.append(si)
    if 1 in si:
        starts.add(i)
    if m in si:
        goals.add(i)

    for sij in si:
        t[sij].add(i)

edges = [set() for _ in range(n)]

for i in range(n):
    for sij in s[i]:
        for k in t[sij]:
            if i == k:
                continue
            edges[i].add(k)
            edges[k].add(i)

ans = 10 ** 9
for st in starts:
    que = deque()
    que.append((st, 0))
    while que:
        cur = que.popleft()
        if cur[0] in goals:
            ans = min(ans, cur[1])
            break
        for sij in edges[cur[0]]:
            que.append((sij, cur[1] + 1))
if ans == 10 ** 9:
    print(-1)
else:
    print(ans)
