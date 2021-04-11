import math
A, B, W = map(int, input().split())
W = W * 1000

max_num = math.floor(W / A)
min_num = math.ceil(W / B)
if B * max_num < W or A * min_num > W:
    print("UNSATISFIABLE")
    exit()

print(min_num, max_num)

