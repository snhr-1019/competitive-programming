# 各yについて、Lの人で一番右にいる人、Rの人で一番左にいる人を覚える
# mostLeftR < mostRightL となっていたら衝突

n = int(input())
X = [0] * n
Y = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    X[i] = x
    Y[i] = y
S = input()

ls = []

for i in range(n):
    ls.append((Y[i], X[i], S[i]))
ls.sort()

cur_y = ls[0][0]
minR = 10 ** 9 + 10
maxL = -1
for i in range(n):
    if i == n - 1 or cur_y != ls[i][0]:
        cur_y = ls[i][0]
        if minR <= maxL:
            print("Yes")
            exit()
        minR = 10 ** 9 + 10
        maxL = -1

    if ls[i][2] == "R":
        minR = min(minR, ls[i][1])
    else:
        maxL = max(maxL, ls[i][1])
print("No")
