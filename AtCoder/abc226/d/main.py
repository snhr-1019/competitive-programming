N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

grads = set()
ans = 0
inf = False
for i in range(N - 1):
    for j in range(i + 1, N):
        x = X[i] - X[j]
        y = Y[i] - Y[j]
        if x == 0:
            if not inf:
                inf = True
                ans += 2
        else:
            grad = y / x
            if grad not in grads:
                grads.add(grad)
                ans += 2
print(ans)
