N = int(input())
A = list(map(int, input().split()))
A = A + [-1]

ans = 0
for i in range(N):
    for j in range(i, N + 1):
        if A[i] > A[j]:
            ans = max(ans, A[i] * (j - i))
            break
print(ans)
