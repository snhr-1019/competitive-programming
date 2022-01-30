h, w = map(int, input().split())
a = []
for i in range(h):
    a.append(list(map(int, input().split())))

b = [[0] * h for i in range(w)]
for i in range(w):
    for j in range(h):
        b[i][j] = a[j][i]

for i in range(w):
    print(*b[i])
