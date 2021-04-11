N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

diff = []
for i in range(N-1):
    diff.append(A[i] - A[i+1])

ans = 0
for i in range(N-1):
    ans += diff[i] * (N-1-i) * (i+1)
print(ans)

