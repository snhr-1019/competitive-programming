ha, wa = map(int, input().split())
a = [list(input()) for _ in range(ha)]
a_black = []
for i in range(ha):
    for j in range(wa):
        if a[i][j] == "#":
            a_black.append((i, j))

hb, wb = map(int, input().split())

b = [list(input()) for _ in range(hb)]
b_black = []
for i in range(hb):
    for j in range(wb):
        if b[i][j] == "#":
            b_black.append((i, j))

hx, wx = map(int, input().split())
x = [list(input()) for _ in range(hx)]
x_black = set()
for i in range(hx):
    for j in range(wx):
        if x[i][j] == "#":
            x_black.add((i, j))

for xb in x_black:
    black = set()

    for ab in a_black:
        black.add((ab[0] + xb[0], ab[1] + xb[1]))

    for xb2 in x_black:
        for bb in b_black:
            black.add((bb[0] + xb2[0], bb[1] + xb2[1]))

        if black == x_black:
            print("Yes")
            exit()

print("No")
