from collections import deque

n = int(input())
p = [[0]]
for i in range(n):
    t = list(map(int, input().split()))
    p.append(t[1:])

ans = []
read = [False] * (n + 1)
que = deque([1])
while que:
    cur = que.popleft()
    for nxt in p[cur]:
        if not read[nxt]:
            que.append(nxt)
            ans.append(nxt)
            read[nxt] = True
print(*ans[::-1])
