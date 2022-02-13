n, k = map(int, input().split())
a = list(map(int, input().split()))
a_dict = {x: i for i, x in enumerate(sorted(a))}

base = k // n
rest = k % n
for i in range(n):
    r = 1 if a_dict[a[i]] < rest else 0
    print(base + r)
