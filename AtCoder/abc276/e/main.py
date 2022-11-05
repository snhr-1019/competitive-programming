import sys

sys.setrecursionlimit(10 ** 6)

h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == 'S':
            x = i
            y = j
            break
    else:
        continue
    break


def dfs(x, y, l):
    if x < 0 or x >= h or y < 0 or y >= w:
        return

    # 壁か既に通ったマスならNG
    if grid[x][y] == '#' or visited[x][y]:
        return

    if l < 4 and grid[x][y] == 'S':
        return

    if l >= 4 and grid[x][y] == 'S':
        print("Yes")
        exit()
    visited[x][y] = True
    dfs(x + 1, y, l + 1)
    dfs(x - 1, y, l + 1)
    dfs(x, y + 1, l + 1)
    dfs(x, y - 1, l + 1)
    visited[x][y] = False


dfs(x + 1, y, 1)
dfs(x - 1, y, 1)
dfs(x, y + 1, 1)
dfs(x, y - 1, 1)
print("No")
