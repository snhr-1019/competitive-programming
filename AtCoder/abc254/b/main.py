n = int(input())

a = [1]
print(*a)
for i in range(1, n):
    a = a + [0]
    b = a[:]
    for j in range(1, i + 1):
        b[j] = a[j - 1] + a[j]
    print(*b)
    a = b
