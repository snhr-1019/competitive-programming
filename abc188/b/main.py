n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

product = 0
for i in range(n):
    product += a[i] * b[i]

if product == 0:
    print('Yes')
else:
    print('No')
