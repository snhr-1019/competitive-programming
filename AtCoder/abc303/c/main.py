n, m, h, k = map(int, input().split())
s = list(input())

d = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

items = set()
for i in range(m):
    items.add(tuple(map(int, input().split())))

cx, cy = (0, 0)
for si in s:
    dx, dy = d[si]
    cx += dx
    cy += dy
    h -= 1
    if h < 0:
        print("No")
        exit()

    if (cx, cy) in items and h < k:
        h = k
        items.remove((cx, cy))
print("Yes")
