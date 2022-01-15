h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for i in range(h - 1):
    for j in range(w - 1):
        diff = b[i][j] - a[i][j]
        ans += abs(diff)

        a[i][j] += diff
        a[i + 1][j] += diff
        a[i][j + 1] += diff
        a[i + 1][j + 1] += diff
    if a[i][w - 1] != b[i][w - 1]:
        print("No")
        exit()
if a[h - 1] != b[h - 1]:
    print("No")
else:
    print("Yes")
    print(ans)
