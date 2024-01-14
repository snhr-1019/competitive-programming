n = int(input())
x, y, z = 0, 0, -1
for i in range((n + 1) ** 3):
    z += 1
    if z > n:
        z = 0
        y += 1

    if y > n:
        y = 0
        x += 1

    if x + y + z <= n:
        print(x, y, z)
