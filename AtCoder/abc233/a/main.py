import math
X, Y = map(int, input().split())
print(max(0, int(math.ceil((Y - X) / 10))))
