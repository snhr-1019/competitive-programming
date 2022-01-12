n = int(input())
a = list(map(int, input().split()))
K = sum(a) / 10

s = a[0]
j = 0
for i in range(n):
    while True:
        if s == K:
            print("Yes")
            exit()
        elif s > K:
            break

        j = (j + 1) % n
        s += a[j]
    s -= a[i]

print("No")
