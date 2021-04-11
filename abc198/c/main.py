import math

R, X, Y = map(int, input().split())
a = (X ** 2 + Y ** 2) ** 0.5 / R
if a < 1:
    print(2)
else:
    print(int(math.ceil(a)))
