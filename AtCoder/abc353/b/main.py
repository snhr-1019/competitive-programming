n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
i = 0
while i < n:
    ans += 1
    vacant = k

    while i < n and vacant >= a[i]:
        vacant -= a[i]
        i += 1
print(ans)
