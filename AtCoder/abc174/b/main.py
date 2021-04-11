import math

n, d = map(int, input().split())

points = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for i in range(n):
    if math.sqrt(points[i][0] ** 2 + points[i][1] ** 2) <= d:
        cnt += 1

print(cnt)
