n = int(input())

x = [0] * n
y = [0] * n
for i in range(n):
    t, s = map(int, input().split())
    x[i] = t
    y[i] = s

x.sort()
y.sort()

if n % 2 == 0:
    c = n // 2
    ex_2 = x[c - 1] + x[c]
    ey_2 = y[c - 1] + y[c]
else:
    c = n // 2
    ex_2 = x[c] * 2
    ey_2 = y[c] * 2
sx = 0
sy = 0
for i in range(n):
    sx += abs(x[i] * 2 - ex_2)
    sy += abs(y[i] * 2 - ey_2)
ans = (sx + sy) // 2
print(ans)
