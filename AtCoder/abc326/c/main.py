from bisect import bisect_left

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    ans = max(ans, bisect_left(a, a[i] + m) - i)
print(ans)
