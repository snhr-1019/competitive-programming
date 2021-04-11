N = int(input())
A = list(map(int, input().split()))
A = A + [-1]

ans = 0
for l in range(N):
    min_cost = 10 ** 9 + 1
    for r in range(l, N + 1):
        if min_cost > A[r]:
            ans = max(ans, min_cost * (r - l))
            min_cost = A[r]
print(ans)
