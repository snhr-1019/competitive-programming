N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

ans = True
for j in range(M):
    if j > 0 and B[0][j - 1] + 1 != B[0][j]:
        ans = False

    if j != M - 1 and B[0][j] % 7 == 0:
        ans = False

for i in range(1, N):
    for j in range(M):
        if B[i - 1][j] + 7 != B[i][j]:
            ans = False

if ans:
    print("Yes")
else:
    print("No")
