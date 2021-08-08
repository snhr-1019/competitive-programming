H, W, N = map(int, input().split())

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append([a, i])
    B.append([b, i])

A.sort()
B.sort()

a = 1
b = 1
A[0].append(a)
B[0].append(b)
for i in range(1, N):
    if A[i - 1][0] != A[i][0]:
        a += 1
    if B[i - 1][0] != B[i][0]:
        b += 1
    A[i].append(a)
    B[i].append(b)

A.sort(key=lambda x: x[1])
B.sort(key=lambda x: x[1])

for i in range(N):
    print(str(A[i][2]) + ' ' + str(B[i][2]))
