r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
bombs = []
ans = [[""] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if b[i][j] not in ("#", "."):
            bombs.append((i, j))


def manhattan(i1, j1, i2, j2):
    return abs(i1 - i2) + abs(j1 - j2)


def is_empty(i, j):
    if b[i][j] == ".":
        return True

    return any(manhattan(i, j, bi, bj) <= int(b[bi][bj]) for (bi, bj) in bombs)


for i in range(r):
    for j in range(c):
        if is_empty(i, j):
            ans[i][j] = "."
        else:
            ans[i][j] = "#"

for i in range(r):
    print("".join(ans[i]))
