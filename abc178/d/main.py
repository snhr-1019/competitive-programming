
def dfs(n, rest):
    mod = 1000000007
    global S
    if rest == 0:
        return 1
    elif rest < 0:
        return 0

    ans = dfs(3, rest - 3)

    for i in range(4, rest + 1):
        ans += dfs(i, rest - i)
        ans %= mod
    return ans


S = int(input())

print(dfs(0, S))
