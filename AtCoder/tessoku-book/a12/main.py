n, k = map(int, input().split())
a = list(map(int, input().split()))


# 答えがx秒以下か否か
def check(x):
    s = 0
    for ai in a:
        s += x // ai
    return s >= k


l = 0
r = 10 ** 9 + 1
while l < r:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m + 1
print(l)
