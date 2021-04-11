N = int(input())
A = [0] + list(map(int, input().split()))
N += 1
accum_sum = [0] * N
accum_max = [0] * N
accum_sum[0] = A[0]
accum_max[0] = A[0]

for i in range(1, N):
    accum_sum[i] = accum_sum[i - 1] + A[i]
    accum_max[i] = max(accum_max[i - 1], accum_sum[i])

ans = 0
x = 0
for i in range(1, N):
    ans = max(ans, x + accum_max[i])
    x += accum_sum[i]
print(ans)
