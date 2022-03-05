import sys

sys.setrecursionlimit(10 ** 7)

s = list(map(lambda x: ord(x) - ord('A'), list(input())))
q = int(input())


def f(t, k):
    if t == 0:
        return s[k]
    if k == 0:
        return (s[k] + t % 3) % 3

    if k % 2 == 0:
        d = 1
    else:
        d = 2
    return (f(t - 1, k // 2) + d) % 3


def solve():
    t, k = map(int, input().split())
    k -= 1

    print(chr(ord('A') + f(t, k)))


for i in range(q):
    solve()
