n = int(input())
M = 46
cnt = [[0] * M for _ in range(3)]
for i in range(3):
    a = list(map(int, input().split()))
    for t in a:
        cnt[i][t % M] += 1

ans = 0
for i in range(M):
    for j in range(M):
        k = (M - i - j) % M
        ans += cnt[0][i] * cnt[1][j] * cnt[2][k]
print(ans)
