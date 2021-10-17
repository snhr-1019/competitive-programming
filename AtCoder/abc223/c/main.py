N = int(input())
A = []
B = []
t = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    t += a / b
t /= 2
ans = 0
for i in range(N):
    if t > A[i] / B[i]:
        ans += A[i]
        t -= A[i] / B[i]
    else:
        ans += B[i] * t
        break
print(ans)
