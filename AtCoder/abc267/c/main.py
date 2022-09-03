n, m = map(int, input().split())
a = list(map(int, input().split()))

acc = [0] * (n + 1)

for i in range(n):
    acc[i + 1] = acc[i] + a[i]

cur = 0
for i in range(m):
    cur += (i + 1) * a[i]
ans = cur

for i in range(m, n):
    cur += m * a[i]
    cur -= acc[i] - acc[i - m]
    ans = max(cur, ans)

print(ans)
