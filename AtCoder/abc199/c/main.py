N = int(input())
S = input()
Q = int(input())

Ts = []
As = []
Bs = []

S = list(S)
reverse = False

for i in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if reverse:
            if a < N:
                a += N
            else:
                a -= N
            if b < N:
                b += N
            else:
                b -= N

        tmp = S[a]
        S[a] = S[b]
        S[b] = tmp
    else:
        reverse = not reverse

if reverse:
    print(''.join(S[N:2 * N] + S[0:N]))
else:
    print(''.join(S))
