import math

A, B, C, D = map(int, input().split())

diff = C * D - B
if diff <= 0:
    print(-1)
    exit()

ans = math.ceil(A / diff)
print(ans)
