from collections import deque

N, M = map(int, input().split())
route = [[] for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    route[a].append(b)

ans = 0
for start in range(1, N + 1):
    todo = deque()
    todo.append(start)
    seen = [False] * (N + 1)
    seen[start] = True
    while todo:
        cur = todo.popleft()
        for nxt in route[cur]:
            if not seen[nxt]:
                todo.append(nxt)
                seen[nxt] = 1
    ans += sum(seen)
print(ans)
