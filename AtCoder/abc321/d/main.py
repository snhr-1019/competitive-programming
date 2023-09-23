from bisect import bisect_left

n, m, p = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

acc_b = [0] * (m + 1)
for i in range(1, m + 1):
    acc_b[i] = acc_b[i - 1] + b[i - 1]
ans = 0
for ai in a:
    bs = bisect_left(b, p - ai)
    ans += acc_b[bs] + ai * bs
    ans += (m - bs) * p
print(ans)
