x, y, z = map(int, input().split())

if not (0 < y < x or x < y < 0):
    print(abs(x))
elif (0 < z < y < x) or (x < y < z < 0):
    print(abs(x))
elif z < 0 < y < x or x < y < 0 < z:
    print(2 * abs(z) + abs(x))
else:
    print(-1)
