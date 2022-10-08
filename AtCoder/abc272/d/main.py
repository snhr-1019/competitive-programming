from collections import deque

n, m = map(int, input().split())

grid = [[-1] * n for _ in range(n)]
grid[0][0] = 0


def d2(x, y, i, j):
    return (i - x) ** 2 + (j - y) ** 2


dist = set()
for i in range(-n, n):
    for j in range(-n, n):
        if d2(0, 0, i, j) == m:
            dist.add((i, j))

q = deque()
q.append((0, 0))

while q:
    cur = q.popleft()
    x = cur[0]
    y = cur[1]
    for d in dist:
        i = x + d[0]
        j = y + d[1]
        if 0 <= i < n and 0 <= j < n and grid[i][j] == -1:
            grid[i][j] = grid[x][y] + 1
            q.append((i, j))

for g in grid:
    print(*g)
