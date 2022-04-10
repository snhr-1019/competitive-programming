n, x, y = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for l in range(n):
    r = l
    min_v = a[l]
    max_v = a[l]
    while r < n:
        min_v = min(min_v, a[r])
        max_v = max(max_v, a[r])
        if min_v == y and max_v == x:
            ans += 1
        if min_v < y or max_v > x:
            break
        r += 1
print(ans)
