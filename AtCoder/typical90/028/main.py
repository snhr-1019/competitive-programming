N = int(input())
grid = [[0] * 1000 for _ in range(1000)]

for i in range(N):
    lx, ly, rx, ry = map(lambda x: int(x) - 1, input().split())
    grid[lx][ly] += 1
    grid[lx][ry] -= 1
    grid[rx][ly] -= 1
    grid[rx][ry] += 1
    for k in range(10):
        print(grid[k][:10])



accum = [[0] * 1001 for _ in range(1001)]
# 横方向の累積和
for i in range(1000):
    for j in range(1000):
        accum[i][j + 1] = accum[i][j] + grid[i][j]

