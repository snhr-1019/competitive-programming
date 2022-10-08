n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))

acc = [0] * (n + 1)
acc[0] = 0
for i in range(n):
    acc[i + 1] = acc[i] + a[i]
acc_s = set(acc)

for i in range(n):
    if p + acc[i] in acc_s and p + q + acc[i] in acc_s and p + q + r + acc[i] in acc_s:
        print("Yes")
        exit()
print("No")
