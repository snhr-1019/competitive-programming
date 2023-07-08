import copy

n = int(input())
a = [list(input()) for _ in range(n)]
ans = copy.deepcopy(a)

for i in range(1, n):
    ans[0][i] = a[0][i - 1]

for i in range(1, n):
    ans[i][-1] = a[i - 1][-1]

for i in range(1, n):
    ans[-1][~i] = a[-1][~(i - 1)]

for i in range(1, n):
    ans[~i][0] = a[~(i - 1)][0]

for x in ans:
    print(*x, sep='')
