n, k = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()
n = len(a)
ans = 0
for i in range(n):
    if a[i] == i:
        ans += 1
        ans = min(ans, k)
print(ans)