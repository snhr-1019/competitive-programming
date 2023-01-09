n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
acc = [0] * (n + 1)
for i in range(1, n + 1):
    acc[i] = acc[i - 1] + a[i]

for i in range(q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l - 1])
