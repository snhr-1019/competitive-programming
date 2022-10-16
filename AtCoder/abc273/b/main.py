x, k = map(int, input().split())

for i in range(1, k + 1):
    r = x % 10 ** i
    x -= r
    if 5 * 10 ** (i - 1) <= r:
        x += 10 ** i
print(x)
