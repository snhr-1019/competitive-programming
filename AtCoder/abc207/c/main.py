n = int(input())
L = [0] * n
R = [0] * n
for i in range(n):
    t, l, r = map(int, input().split())
    if t == 1:
        pass
    elif t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    L[i] = l
    R[i] = r

ans = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        ans += (max(L[i], L[j]) <= min(R[i], R[j]))
print(ans)
