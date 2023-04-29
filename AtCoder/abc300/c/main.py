h, w = map(int, input().split())
c = [list(input()) + ['.'] for _ in range(h)]
c += [['.'] * (w + 1)]
checked = [[False] * w for _ in range(h)]

n = min(h, w)
ans = [0] * n
for i in range(h):
    for j in range(w):
        if checked[i][j]:
            continue

        if c[i][j] == "#":
            ci, cj = i, j

            while c[ci][cj] == "#":
                checked[ci][cj] = True
                ci += 1
                cj += 1
            size = (ci - i) // 2
            ans[size - 1] += 1

            mi, mj = i + size, j + size
            for k in range(1, size + 1):
                checked[mi - k][mj + k] = True
                checked[mi + k][mj - k] = True
print(*ans)
