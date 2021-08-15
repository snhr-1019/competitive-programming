N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
R = [0] * N

minT = T.index(min(T))
R[minT] = T[minT]
for i in range(minT + 1, minT + N + 1):
    i %= N
    R[i] = min(R[(i - 1) % N] + S[(i - 1) % N], T[i])

for r in R:
    print(r)

