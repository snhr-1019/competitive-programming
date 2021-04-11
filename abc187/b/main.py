N = int(input())
x = []
y = []


def calc_gradient(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


for i in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        if -1 <= calc_gradient(x[i], y[i], x[j], y[j]) <= 1:
            ans += 1
print(ans)
