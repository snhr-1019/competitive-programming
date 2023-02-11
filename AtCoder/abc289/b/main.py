import sys

sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())
a = [False] * (n + 1)

tmp = list(map(int, input().split()))
for t in tmp:
    a[t] = True


def get(i):
    if a[i]:
        d = get(i + 1)
        d.append(i)
        return d
    else:
        return [i]


ans = []
cur = 1

ans = []
while cur <= n:
    d = get(cur)
    cur = d[0] + 1
    ans += d
print(*ans)
