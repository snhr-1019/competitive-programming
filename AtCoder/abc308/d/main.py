from collections import deque

h, w = map(int, input().split())

s = [['z'] * (w + 2)]
for _ in range(h):
    s.append(['z'] + list(input()) + ['z'])
s.append(['z'] * (w + 2))

target = 'snuke'

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

stack = deque()

visited = [[False] * (w + 2) for _ in range(h + 2)]
stack.append((1, 1, 0))
while stack:
    i, j, k = stack.popleft()

    if visited[i][j] or s[i][j] != target[k]:
        continue

    visited[i][j] = True
    for di, dj in d:
        stack.append((i + di, j + dj, (k + 1) % len(target)))

if visited[h][w]:
    print("Yes")
else:
    print("No")
