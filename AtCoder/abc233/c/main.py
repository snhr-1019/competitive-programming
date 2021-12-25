import sys

sys.setrecursionlimit(20000000)

N, X = map(int, input().split())
L = [0] * N
a = []

global ans
ans = 0


# 1つ前までの積がproduct, pos番目の数字を選ぶ
def dfs(pos, product):
    global ans
    for i in range(L[pos]):
        if product > product * a[pos][i] > X:
            break
        if pos < N - 1:
            dfs(pos + 1, product * a[pos][i])
        elif pos == N - 1 and product * a[pos][i] == X:
            ans += 1


for i in range(N):
    tmp = list(map(int, input().split()))
    L[i] = tmp[0]
    a.append(sorted(tmp[1:]))

dfs(0, 1)
print(ans)
