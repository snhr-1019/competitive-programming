h, w = map(int, input().split())
x = [[0] * (w + 1)]
for _ in range(h):
    x.append([0] + list(map(int, input().split())))

acc = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        acc[i][j] = acc[i][j - 1] + x[i][j]

for j in range(1, w + 1):
    for i in range(1, h + 1):
        acc[i][j] = acc[i - 1][j] + acc[i][j]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(acc[c][d] + acc[a - 1][b - 1] - acc[a - 1][d] - acc[c][b - 1])
