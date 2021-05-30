N, K = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))
A.sort(key=lambda x: x[0])

now = 0
for i in range(N):
    a = A[i][0]
    b = A[i][1]
    if K >= a - now:
        K = K - (a - now) + b
        now = a
    else:
        print(now + K)
        exit(0)
print(now + K)
exit(0)

