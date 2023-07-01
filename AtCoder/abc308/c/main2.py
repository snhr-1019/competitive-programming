from functools import cmp_to_key

n = int(input())

f = []

for i in range(n):
    a, b = map(int, input().split())
    f.append((a, b, -(i + 1)))


def cmp(arg1, arg2):
    t1 = arg1[0] * (arg2[1] - arg2[0])
    t2 = arg2[0] * (arg1[1] - arg1[0])
    if t1 == t2:
        return -1 if arg1[2] < arg2[2] else 1
    return -1 if t1 < t2 else 1


f.sort(reverse=True, key=cmp_to_key(cmp))

ans = []
for fi in f:
    print(-fi[2])
