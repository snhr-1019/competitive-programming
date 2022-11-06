from collections import deque

h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]
cnt = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'S':
            x = i
            y = j
            break
    else:
        continue
    break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy):
    visited = [[False] * w for _ in range(h)]
    que = deque()
    que.append((sx, sy))

    while que:
        x, y = que.popleft()
        # 範囲外
        if x < 0 or x >= h or y < 0 or y >= w:
            continue

        # 壁か既に通ったマスならNG
        if grid[x][y] in ('#', 'S') or visited[x][y]:
            continue
        cnt[x][y] += 1
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            que.append((nx, ny))


for i in range(4):
    bfs(x + dx[i], y + dy[i])

for i in range(h):
    for j in range(w):
        if cnt[i][j] >= 2:
            print("Yes")
            exit()
print("No")
