h, w, n = map(int, input().split())
grid = [[0] * (w + 10) for _ in range(h + 10)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[a][d + 1] -= 1
    grid[c + 1][b] -= 1
    grid[c + 1][d + 1] += 1

acc = [[0] * (w + 10) for _ in range(h + 10)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        acc[i][j] = acc[i][j - 1] + grid[i][j]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        acc[i][j] += acc[i - 1][j]

for i in range(1, h + 1):
    print(*acc[i][1:w + 1])
