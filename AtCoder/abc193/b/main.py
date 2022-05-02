n = int(input())
APX = []
for i in range(n):
    APX.append(list(map(int, input().split())))
APX.sort()

INF = 10 ** 9 + 10
ans = INF
for i in range(n):
    if APX[i][2] - APX[i][0] > 0:
        ans = min(ans, APX[i][1])
if ans == INF:
    print(-1)
else:
    print(ans)
