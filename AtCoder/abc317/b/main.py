n = int(input())
a = sorted(list(map(int,input().split())))
for i in range(n):
    if a[i] != a[0] + i:
        print(a[0] + i)
        exit()
