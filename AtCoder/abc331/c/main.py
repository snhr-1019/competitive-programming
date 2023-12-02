from bisect import bisect_right

n = int(input())
a = list(map(int, input().split()))
s = sorted(a)

acc = [0] * (n + 1)

for i in range(n):
    acc[i + 1] = acc[i] + s[i]

ans = [0] * n
for i in range(n):
    ans[i] = acc[-1] - acc[bisect_right(s, a[i])]
print(*ans)