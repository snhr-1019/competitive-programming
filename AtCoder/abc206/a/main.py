import math

N = int(input())
p = math.floor(N * 1.08)

if p > 206:
    print(":(")
elif p == 206:
    print("so-so")
else:
    print("Yay!")
