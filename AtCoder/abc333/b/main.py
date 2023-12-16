s = list(input())
t = list(input())


def f(x):
    return ord(x) - ord('a')


def d(x):
    t = abs(f(x[0]) - f(x[1]))
    return min(t, 5 - t)


if d(s) == d(t):
    print('Yes')
else:
    print('No')
