N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
    out = []
    for j in range(R, S + 1):
        if abs(A - i) == abs(B - j):
            out.append("#")
        else:
            out.append(".")
    print(''.join(out))
