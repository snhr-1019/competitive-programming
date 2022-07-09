import math

a, b, d = map(int, input().split())

theta = d / 360 * 2 * math.pi

x = a * math.cos(theta) - b * math.sin(theta)
y = a * math.sin(theta) + b * math.cos(theta)

print(x, y)
