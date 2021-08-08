N, M = map(int, input().split())
A = [[int(x), 0] for x in input().split()]
B = [[int(x), 1] for x in input().split()]
C = sorted(A + B)

ans = 10 ** 9 + 1

for i in range(N + M - 1):
    if C[i][1] != C[i + 1][1]:
        ans = min(ans, C[i + 1][0] - C[i][0])
print(ans)
