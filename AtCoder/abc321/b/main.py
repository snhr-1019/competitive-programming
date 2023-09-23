n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))

if sum(a[1:-2]) >= x:
    print(0)
else:
    d = x - sum(a[1:-1])
    if d <= a[0]:
        print(0)
    elif a[0] < d <= a[-1]:
        print(d)
    else:
        print(-1)
