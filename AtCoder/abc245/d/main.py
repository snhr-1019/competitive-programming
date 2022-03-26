n, m = map(int, input().split())
n += 1
m += 1
a = list(map(int, input().split()))
a.reverse()
b = [0] * m
c = list(map(int, input().split()))
c.reverse()

cur = c[:]
for i in range(m):
    b[i] = cur[i] // a[0]

    for j in range(n):
        cur[i + j] -= a[j] * b[i]

b.reverse()
print(*b)
