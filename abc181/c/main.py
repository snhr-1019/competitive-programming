N = int(input())
x = []
y = []
for i in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if (x[k] - x[i]) * (y[j] - y[i]) == (x[j] - x[i]) * (y[k] - y[i]):
                print('Yes')
                exit(0)
print('No')
