h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

row = [False] * h
col = [False] * w
while True:
    diff = False

    new_row = row[:]
    for i in range(h):
        if row[i]:
            continue
        color = set()
        cnt = 0
        for j in range(w):
            if col[j]:
                continue
            color.add(c[i][j])
            cnt += 1
        if cnt >= 2 and len(color) == 1:
            new_row[i] = True
            diff = True

    new_col = col[:]
    for j in range(w):
        if col[j]:
            continue
        color = set()
        cnt = 0
        for i in range(h):
            if row[i]:
                continue
            color.add(c[i][j])
            cnt += 1
        if cnt >= 2 and len(color) == 1:
            new_col[j] = True
            diff = True
    if not diff:
        break
    row = new_row
    col = new_col

print(sum(1 for x in row if not x) * sum(1 for x in col if not x))
