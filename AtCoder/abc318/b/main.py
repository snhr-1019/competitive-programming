n = int(input())
grid = [[False] * 101 for _ in range(101)]

for _ in range(n):
    a, b, c, d = map(lambda x: int(x) - 1, input().split())

    for i in range(a, b):
        for j in range(c, d):
            grid[i][j] = True

ans = 0
for i in range(101):
    for j in range(101):
        ans += grid[i][j]
print(ans)