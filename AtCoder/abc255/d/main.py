from bisect import bisect_left

n, q = map(int, input().split())
a = sorted(map(int, input().split()))
acc = [0] * (n + 1)

for i in range(1, n + 1):
    acc[i] = acc[i - 1] + a[i - 1]


def solve():
    x = int(input())
    b = bisect_left(a, x)

    ln = b
    rn = n - ln
    left = x * ln - acc[b]
    right = (acc[n] - acc[b]) - x * rn
    print(left + right)


for i in range(q):
    solve()
