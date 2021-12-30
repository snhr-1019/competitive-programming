N = int(input())
accum = [[0] * (N + 1) for _ in range(2)]

for i in range(1, N + 1):
    C, P = map(int, input().split())
    C -= 1
    accum[C][i] += accum[C][i - 1] + P
    another = not C
    accum[another][i] += accum[another][i - 1]

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    print(accum[0][R + 1] - accum[0][L], accum[1][R + 1] - accum[1][L])
