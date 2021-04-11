H, W = map(int, input().split())

min_val = 100
A = []
for i in range(H):
    A.append(list(map(int, input().split())))
    min_val = min(min_val, min(A[i]))

ans = 0

for i in range(H):
    for j in range(W):
        ans += A[i][j] - min_val

print(ans)