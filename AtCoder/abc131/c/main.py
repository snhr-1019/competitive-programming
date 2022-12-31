from math import gcd

a, b, c, d = map(int, input().split())


def cnt(n):
    return b // n - (a + n - 1) // n + 1


def lcm(a, b):
    return a * b // gcd(a, b)


print(cnt(1) - cnt(c) - cnt(d) + cnt(lcm(c, d)))
