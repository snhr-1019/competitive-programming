n = int(input())
A = list(map(int, input().split()))

f2 = [0] * n
f3 = [0] * n
fo = [0] * n
for i, a in enumerate(A):
    while a % 2 == 0:
        a //= 2
        f2[i] += 1
    while a % 3 == 0:
        a //= 3
        f3[i] += 1
    fo[i] = a

if len(set(fo)) == 1:
    ans = 0
    m2 = min(f2)
    m3 = min(f3)
    for i in range(n):
        ans += f2[i] - m2
    for i in range(n):
        ans += f3[i] - m3
    print(ans)
else:
    print(-1)