s = []
a = c = 100
b = d = -100
for i in range(10):
    l = list(input())
    for j in range(10):
        if l[j] == "#":
            a = min(i + 1, a)
            b = max(i + 1, b)
            c = min(j + 1, c)
            d = max(j + 1, d)
print(a, b)
print(c, d)
