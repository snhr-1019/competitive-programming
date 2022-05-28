import math

n, a, b = map(int, input().split())


def lcm(a, b):
    return a * b // math.gcd(a, b)


def calc(k):
    l = 0 if n < k else 1
    r = n // k
    return k * (l + r) * (r - l + 1) // 2


ans = n * (n + 1) // 2
ma = calc(a)
ans -= ma

mb = calc(b)
ans -= mb

g = lcm(a, b)
mab = calc(g)
ans += mab
print(ans)
