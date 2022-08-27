def isInside(ax, ay, bx, by, cx, cy, tx, ty):
    abXat = (bx - ax) * (ty - ay) - (by - ay) * (tx - ax)
    bcXbt = (cx - bx) * (ty - by) - (cy - by) * (tx - bx)
    caXct = (ax - cx) * (ty - cy) - (ay - cy) * (tx - cx)
    if (abXat > 0 and bcXbt > 0 and caXct > 0) or (abXat < 0 and bcXbt < 0 and caXct < 0):
        return True
    elif abXat * bcXbt * caXct == 0:
        return False
    return False;


def isConcave(px, py):
    for i in range(4):
        if isInside(px[i % 4], py[i % 4], px[(i + 1) % 4], py[(i + 1) % 4], px[(i + 2) % 4], py[(i + 2) % 4],
                    px[(i + 3) % 4], py[(i + 3) % 4]):
            return True
    return False

px = []
py = []
for i in range(4):
    x, y = map(int, input().split())
    px.append(x)
    py.append(y)

if isConcave(px, py):
    print("No")
else:
    print("Yes")
