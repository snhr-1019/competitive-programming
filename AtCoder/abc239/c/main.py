x1, y1, x2, y2 = map(int, input().split())

candidates = []


def dist2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


for xd in range(-3, 4):
    for yd in range(-3, 4):
        if dist2(x1, y1, x1 + xd, y1 + yd) == 5:
            if dist2(x2, y2, x1 + xd, y1 + yd) == 5:
                print("Yes")
                exit()
print("No")
