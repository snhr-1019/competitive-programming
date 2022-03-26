n, k = map(int, input().split())
ab = []
ab.append(list(map(int, input().split())))
ab.append(list(map(int, input().split())))

ok = [[False] * n for _ in range(2)]
ok[0][0] = True
ok[1][0] = True

for i in range(1, n):
    for j in range(2):
        if ok[j][i - 1]:
            if abs(ab[j][i - 1] - ab[0][i]) <= k:
                ok[0][i] = True
            if abs(ab[j][i - 1] - ab[1][i]) <= k:
                ok[1][i] = True

if ok[0][n - 1] or ok[1][n - 1]:
    print("Yes")
else:
    print("No")
