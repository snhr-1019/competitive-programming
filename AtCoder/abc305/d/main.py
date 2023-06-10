from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
acc = [0] * (n + 1)

for i in range(1, n):
    if i % 2 == 1:
        acc[i + 1] = acc[i]
    else:
        acc[i + 1] = acc[i] + a[i] - a[i - 1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    li = bisect_left(a, l)
    if li % 2 == 0:
        left = a[li] - l
    else:
        left = 0

    ri = bisect_right(a, r)
    if ri % 2 == 0:
        right = r - a[ri - 1]
    else:
        right = 0

    s = acc[ri] - acc[li + 1]
    print(left + s + right)
