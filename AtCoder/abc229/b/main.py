a, b = input().split()
l = max(len(a), len(b))
a = a.zfill(l)
b = b.zfill(l)
for i in range(l):
    if int(a[i]) + int(b[i]) >= 10:
        print('Hard')
        exit()
print('Easy')
