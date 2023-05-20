from bisect import bisect_left, bisect_right

n, m, d = map(int, input().split())

a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))

ans = -1
for ai in a:
    mx = ai + d
    mn = ai - d
    mx_i = bisect_right(b, mx)
    mn_i = bisect_left(b, mn)
    if mn_i == mx_i:
        continue
    ans = max(ans, ai + b[mx_i - 1])
print(ans)
