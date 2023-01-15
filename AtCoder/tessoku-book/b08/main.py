n = int(input())
T = 1501
p = [[0] * T for _ in range(T)]

for _ in range(n):
    x, y = map(int, input().split())
    p[x][y] += 1

acc = [[0] * T for _ in range(T)]

for i in range(1, T):
    for j in range(1, T):
        acc[i][j] = acc[i][j - 1] + p[i][j]

for j in range(1, T):
    for i in range(1, T):
        acc[i][j] += acc[i - 1][j]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(acc[c][d] + acc[a - 1][b - 1] - acc[a - 1][d] - acc[c][b - 1])
