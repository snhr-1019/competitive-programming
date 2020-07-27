n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cnt = 0

for i in range(n):
    t = min(a[i], b[i])
    cnt += t
    a[i] -= t
    b[i] -= t

    s = min(a[i+1], b[i])
    cnt += s
    a[i+1] -= s
    b[i] -= s

print(cnt)