n, q = map(int, input().split())
c = list(map(int, input().split()))
cnt = []
for i in range(1, n):
    cnt[i][c[i]] = cnt[i-1][c[i]]+1

a = 0