N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)
r = X - (X // sumA) * sumA

sm = 0
for i in range(N):
    r -= A[i]
    if r < 0:
        print(X // sumA * N + i + 1)
        exit()
