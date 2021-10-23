from itertools import combinations

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for xy in combinations(XY, 3):
    x0, y0 = xy[0]
    x1, y1 = xy[1]
    x2, y2 = xy[2]

    if (x0 - x2) * (y1 - y2) - (x1 - x2) * (y0 - y2) != 0:
        ans += 1
print(ans)
