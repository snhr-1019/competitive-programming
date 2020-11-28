a, b, x, y = map(int, input().split())

if a == b:
    hall = x
elif a > b:
    # 下に下がる
    hall = (a-b-1)*2*x+x
else:
    # 上に上がる
    hall = (b-a)*2*x+x

print(min((abs(a-b))*y+x, hall))
