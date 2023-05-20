h, w = map(int, input().split())
s = [input() for _ in range(h)]

di = (1, 1, 0, -1, -1, -1, 0, 1)
dj = (0, 1, 1, 1, 0, -1, -1, -1)

t = 'snuke'
for i in range(h):
    for j in range(w):
        for k in range(8):
            if all(
                    0 <= i + di[k] * l < h and
                    0 <= j + dj[k] * l < w and
                    s[i + di[k] * l][j + dj[k] * l] == t[l]
                    for l in range(5)
            ):
                for l in range(5):
                    print(i + di[k] * l + 1, j + dj[k] * l + 1)
