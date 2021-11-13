import math

N = int(input())

ans = 0
for a in range(1, N):
    if a ** 3 > N:
        break
    for b in range(a, N):
        if a * b * b > N:
            break
        ans += int(math.floor(N / (a * b))) - b + 1

if N == 1:
    print(1)
else:
    print(ans)
