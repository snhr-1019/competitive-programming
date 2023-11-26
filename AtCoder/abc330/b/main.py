n, l, r = map(int, input().split())
a = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    if a[i] < l:
        ans[i] = l
    elif a[i] > r:
        ans[i] = r
    else:
        ans[i] = a[i]
print(*ans)
