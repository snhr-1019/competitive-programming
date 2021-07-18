n, x = map(int, input().split())
a = list(map(int, input().split()))

price = 0
for i in range(n):
    if i % 2 == 0:
        price += a[i]
    else:
        price += a[i] - 1
if price <= x:
    print('Yes')
else:
    print('No')
