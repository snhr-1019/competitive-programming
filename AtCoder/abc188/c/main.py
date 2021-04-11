n = int(input())
a = list(map(int, input().split()))
b = list(range(0, 2 ** n))

for i in range(n, 1, -1):
    c = []
    for j in range(0, 2 ** i, 2):
        if a[b[j]] > a[b[j + 1]]:
            c.append(b[j])
        else:
            c.append(b[j + 1])
    b = c[::]

if a[b[0]] > a[b[1]]:
    print(b[1] + 1)
else:
    print(b[0] + 1)
