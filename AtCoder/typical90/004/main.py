H, W = map(int, input().split())
A = []
horizontal_sum = [0] * H
vertical_sum = [0] * W

for i in range(H):
    A.append(list(map(int, input().split())))
    horizontal_sum[i] = sum(A[i])
    for j in range(W):
        vertical_sum[j] += A[i][j]

for i in range(H):
    ans = []
    for j in range(W):
        ans.append(horizontal_sum[i] + vertical_sum[j] - A[i][j])
    print(*ans)
