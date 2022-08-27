import sys

sys.setrecursionlimit(10 ** 8)

n = int(input())

memo = [-1] * (n + 1)


def f(n):
    if memo[n] != -1:
        return memo[n]

    ret = 0
    for i in range(1, 7):
        if n == 1:
            ret += (1 / 6) * i
        else:
            ret += (1 / 6) * (max(i, f(n - 1)))
    memo[n] = ret
    return ret


print(f(n))
