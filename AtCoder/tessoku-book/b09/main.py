n = int(input())
grid = [[0] * 1510 for _ in range(1510)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[a][d] -= 1
    grid[c][b] -= 1
    grid[c][d] += 1

for i in range(1501):
    for j in range(1, 1501):
        grid[i][j] += grid[i][j - 1]

for j in range(1501):
    for i in range(1, 1501):
        grid[i][j] += grid[i - 1][j]

ans = 0
for i in range(1501):
    ans += sum(map(lambda x: x > 0, grid[i][:1501]))

print(ans)
