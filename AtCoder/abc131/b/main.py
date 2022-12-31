n, l = map(int, input().split())
apples = list([l + i for i in range(n)])
mn = 10 ** 10
for a in apples:
    if abs(a) < mn:
        mn = abs(a)
        min_a = a

print(sum(apples) - min_a)
