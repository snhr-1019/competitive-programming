n = int(input())
a = list(map(int, input().split()))

x = -1
for i in range(n):
    if i == n - 1:
        x = a[-1]
        break
    if a[i] > a[i + 1]:
        x = a[i]
        break

ans = list(filter(lambda v: v != x, a))
print(' '.join(map(str, ans)))
