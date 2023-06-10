h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

u = 1000
d = -1
l = 1000
r = -1
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            u = min(u, i)
            d = max(d, i)
            l = min(l, j)
            r = max(r, j)

for i in range(u, d + 1):
    for j in range(l, r + 1):
        if s[i][j] == '.':
            print(i + 1, j + 1)
