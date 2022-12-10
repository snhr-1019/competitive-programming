n, t = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
i = 0

t %= s

while t > a[i]:
    t -= a[i]
    i = (i + 1) % n

print(i + 1, t)
