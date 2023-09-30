from bisect import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    b = bisect(a, i)
    ans.append(a[b] - i - 1)
print(*ans, sep='\n')
