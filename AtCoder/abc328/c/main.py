n, q = map(int, input().split())
s = input()
acc = [0] * (n + 1)
for i in range(1, n):
    acc[i + 1] = acc[i] + (s[i] == s[i - 1])

for _ in range(q):
    l, r = map(int, input().split())
    print(acc[r] - acc[l])
