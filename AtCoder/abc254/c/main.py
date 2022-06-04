n, k = map(int, input().split())
a = list(map(int, input().split()))
sorted_a = sorted(a)

for i in range(k):
    b = sorted(a[i::k])
    for j in range(len(b)):
        a[i + k * j] = b[j]

if sorted_a == a:
    print("Yes")
else:
    print("No")
