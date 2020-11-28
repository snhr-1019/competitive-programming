a, b, x, y = map(int, input().split())

if a == b:
    hall = x
    stair = abs(a - b) * y + x
elif a > b:
    # 下に下がる
    hall = (a - b - 1) * 2 * x + x
    stair = abs(a - b - 1) * y + x
else:
    # 上に上がる
    hall = (b - a) * 2 * x + x
    stair = abs(a - b) * y + x

print(min((stair, hall)))
