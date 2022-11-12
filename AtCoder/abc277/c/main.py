from collections import defaultdict, deque

n = int(input())
l = defaultdict(list)
visited = set()
visited.add(1)

q = deque()
q.append(1)
for _ in range(n):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

ans = 1
while q:
    cur = q.popleft()
    for nxt in l[cur]:
        if nxt not in visited:
            q.append(nxt)
            visited.add(nxt)
            ans = max(ans, nxt)
print(ans)
