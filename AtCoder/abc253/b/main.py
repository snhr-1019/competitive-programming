h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(input())

p = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            p.append((i, j))

print(abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1]))
