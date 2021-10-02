import math

A, B, C = map(int, input().split())
t = int(math.ceil(A / C))
if t * C <= B:
    print(t * C)
else:
    print(-1)

