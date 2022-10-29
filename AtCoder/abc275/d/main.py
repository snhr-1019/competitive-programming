n = int(input())

memo = dict()


def f(x):
    if x in memo.keys():
        return memo[x]

    if x == 0:
        return 1

    ret = f(x // 2) + f(x // 3)
    memo[x] = ret
    return ret


print(f(n))
