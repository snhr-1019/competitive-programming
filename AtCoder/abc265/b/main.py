n, m, t = map(int, input().split())
a = list(map(int, input().split()))

xy = [0] * n
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    xy[x] = y

for i in range(n - 1):
    t += xy[i]
    if t <= a[i]:
        print("No")
        exit()
    t -= a[i]

print("Yes")
