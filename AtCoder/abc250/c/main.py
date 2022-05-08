n, q = map(int, input().split())
balls = [i for i in range(1, n + 1)]
idx = [0] + list(range(n))

for i in range(q):
    x = int(input())
    xi = idx[x]
    yi = xi - 1 if idx[x] == n - 1 else xi + 1
    y = balls[yi]
    balls[xi], balls[yi] = y, x
    idx[x] = yi
    idx[y] = xi

print(*balls)
