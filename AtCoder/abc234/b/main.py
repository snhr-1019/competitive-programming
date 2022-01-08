n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    t, s = map(int, input().split())
    x[i] = t
    y[i] = s


def dist(i, j):
    return (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2


ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans = max(ans, dist(i, j))
print(ans ** 0.5)
