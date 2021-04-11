sx, sy, gx, gy = map(int, input().split())
print(sy / (sy + gy) * (gx - sx) + sx)
