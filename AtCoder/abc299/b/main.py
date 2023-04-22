n, t = map(int, input().split())

max_val = dict()

c = list(map(int, input().split()))
r = list(map(int, input().split()))

for i in range(n):
    if c[i] not in max_val.keys():
        max_val[c[i]] = (c[i], r[i], i + 1)
    else:
        if max_val[c[i]][1] < r[i]:
            max_val[c[i]] = (c[i], r[i], i + 1)

if t in max_val.keys():
    print(max_val[t][2])
else:
    print(max_val[c[0]][2])
