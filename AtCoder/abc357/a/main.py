n, m = map(int, input().split())
h = list(map(int, input().split()))

for i in range(n):
    if m >= h[i]:
        m -= h[i]
    else:
        print(i)
        exit()
print(n)
