import sys

sys.setrecursionlimit(10 ** 9)

MOD = 998244353

n, p = map(int, input().split())

INV = pow(100, -1, MOD)
memo = [-1] * (n + 1)


# ダメージをn与えるために必要な攻撃回数の期待値
def f(n):
    if n <= 0:
        return 0
    if memo[n] != -1:
        return memo[n]
    ret = 1 + (f(n - 2) * p + f(n - 1) * (100 - p)) * INV
    ret %= MOD
    memo[n] = ret
    return ret


print(f(n))
