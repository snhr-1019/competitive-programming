n = int(input())
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0

for an in range(max(q) + 1):
    bn = 10 ** 18
    for i in range(n):
        if q[i] - a[i] * an < 0:
            bn = - 10 ** 18
        elif b[i] > 0:
            bn = min(bn, (q[i] - a[i] * an) // b[i])
    ans = max(ans, an + bn)
print(ans)
