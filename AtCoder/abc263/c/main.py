n, m = map(int, input().split())

lst = [-1] * n


# i番目をkに設定する
def dfs(i, k):
    if i > 0 and lst[i - 1] >= k:
        return
    lst[i] = k

    if i == n - 1:
        print(*lst)
        return
    for r in range(k + 1, m + 1):
        dfs(i + 1, r)


for k in range(1, m + 1):
    dfs(0, k)
