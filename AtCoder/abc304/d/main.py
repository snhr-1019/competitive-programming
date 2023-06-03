w, h = map(int, input().split())
n = int(input())
p = []
q = []
cake = [[0] * (w + 1) for _ in range(h + 1)]
for bi in range(n):
    pi, qi = map(int, input().split())
    cake[qi][pi] = 1

# 2次元累積和を取る
# 横
for y in range(h + 1):
    for x in range(1, w + 1):
        cake[y][x] += cake[y][x - 1]

# 縦
for x in range(w + 1):
    for y in range(1, h + 1):
        cake[y][x] += cake[y - 1][x]

A = int(input())
a = [0] + list(map(int, input().split())) + [w]
B = int(input())
b = [0] + list(map(int, input().split())) + [h]

mn = 10 ** 10
mx = -1

for ai in range(1, A + 2):
    for bi in range(1, B + 2):
        cnt = cake[b[bi]][a[ai]] - cake[b[bi - 1]][a[ai]] - cake[b[bi]][a[ai - 1]] + cake[b[bi - 1]][a[ai - 1]]
        mn = min(mn, cnt)
        mx = max(mx, cnt)
print(mn, mx)
