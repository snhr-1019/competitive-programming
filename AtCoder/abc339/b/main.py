h, w, n = map(int, input().split())

cur = [0, 0]
cur_d = 0
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

grid = [["."] * w for _ in range(h)]

for i in range(n):
    if grid[cur[0]][cur[1]] == ".":
        grid[cur[0]][cur[1]] = "#"
        cur_d = (cur_d + 1) % 4
    else:
        grid[cur[0]][cur[1]] = "."
        cur_d = (cur_d - 1) % 4
    cur[0] = (cur[0] + d[cur_d][0]) % h
    cur[1] = (cur[1] + d[cur_d][1]) % w

for i in range(h):
    print("".join(grid[i]))
