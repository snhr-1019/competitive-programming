H, W, X, Y = map(int, input().split())
grid = [['#'] * (W + 1)]

for i in range(H):
    grid.append(['#'] + list(input()) + ['#'])
grid.append(['#'] * (W + 1))

ans = 1
x = X
y = Y
while True:
    x += 1
    if grid[x][y] == '#':
        break
    ans += 1

x = X
y = Y
while True:
    x -= 1
    if grid[x][y] == '#':
        break
    ans += 1

x = X
y = Y
while True:
    y += 1
    if grid[x][y] == '#':
        break
    ans += 1

x = X
y = Y
while True:
    y -= 1
    if grid[x][y] == '#':
        break
    ans += 1

print(ans)
